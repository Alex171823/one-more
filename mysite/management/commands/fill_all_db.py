from random import randint, uniform

from django.core.management.base import BaseCommand

from faker import Faker

from mysite.models import Author,  Book, Publisher, Store

fake = Faker()


class Command(BaseCommand):
    help = u'Fills database with some data'  # noqa A003

    # fills db with 10 publishers, 15 stores and 20 authors
    def handle(self, *args, **kwargs):
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        # create 5 publishers
        publishers = [Publisher(name=f"Publisher{index}") for index in range(1, 6)]
        Publisher.objects.bulk_create(publishers)

        # create 10 authors
        authors = [Author(name=fake.name(),
                          age=randint(18, 99)) for i in range(0, 10)]
        Author.objects.bulk_create(authors)

        # create 20 books for every publishers
        counter = 0
        books = []
        for publisher in Publisher.objects.all():
            for i in range(20):
                counter = counter + 1
                books.append(Book(name=fake.word().title(),
                                  pages=randint(100, 1100),
                                  price=uniform(300, 900),
                                  rating=randint(1, 10),
                                  pubdate=fake.date(),
                                  publisher=publisher))
        Book.objects.bulk_create(books)

        # create 10 stores and insert 10 books in every store
        books = list(Book.objects.all())
        for i in range(10):
            temp_books = [books.pop(0) for i in range(10)]
            store = Store.objects.create(name=f"Store{i + 1}")
            store.books.set(temp_books)
            store.save()

        # create author for each book
        amount_authors = len(Author.objects.all())
        for book in Book.objects.all():
            author = Author.objects.get(id=randint(1, amount_authors))
            book.authors.add(author)

        self.stdout.write('done')

        # # fill table AuthorBookManyToMany
        # amount_authors = len(Author.objects.all())
        # mtom = []
        # for book in Book.objects.all():
        #     mtom.append(AuthorBookManyToMany(book_id=book,
        #                                      author_id=Author.objects.get(id=randint(1, amount_authors))))
        # AuthorBookManyToMany.objects.bulk_create(mtom)
        #
        # # update book-to-author relations
        # for author in AuthorBookManyToMany.objects.all():
        #     books.append(Book())
