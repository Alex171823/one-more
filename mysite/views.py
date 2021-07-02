from django.db.models import Count, Max, Min, Prefetch
from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Book, Publisher, Store


def start(request):
    return HttpResponse("StartPage")


def authors(request):
    authors = Author.objects.all().annotate()

    return render(request, 'mysite/authors.html', {'authors': authors})


def author_detail(request, pk):
    info_about = Author.objects.get(id=pk)

    books = Book.objects.filter(authors__id=pk)

    stores = Store.objects.filter(books__authors__id=pk)

    publeshers = Publisher.objects.filter(book__authors=pk).distinct()

    return render(request, 'mysite/author_detail.html', {'name': info_about.name,
                                                         'age': info_about.age,
                                                         'books': books,
                                                         'id': info_about.id,
                                                         'stores': stores,
                                                         'num': len(books),
                                                         'publishers': publeshers})


def publisher(request):
    publishers = Publisher.objects.all()

    return render(request, 'mysite/publishers.html', {'publishers': publishers})


def publisher_detail(request, pk):
    info_about = Publisher.objects.get(id=pk)

    list_books = Book.objects.filter(publisher_id=pk)

    queryset = Store.objects.prefetch_related(Prefetch('books', queryset=Book.objects.filter(publisher_id=pk)))
    stores = []
    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'name': store.name, 'books': books})
    # stores = Store.objects.filter(books__publisher_id=pk).distinct() - the same

    return render(request, 'mysite/publisher_detail.html', {'id': info_about.id,
                                                            'name': info_about.name,
                                                            'books': list_books,
                                                            'num': len(list_books),
                                                            'stores': stores,
                                                            })


def store(request):
    stores = Store.objects.all()

    return render(request, 'mysite/stores.html', {'stores': stores})


def store_detail(request, pk):
    info_about = Store.objects.get(id=pk)

    books = Book.objects.filter(store__id=pk)

    price = Book.objects.filter(store__id=pk).aggregate(max=Max('price'), min=Min('price'))

    return render(request, 'mysite/store_detail.html', {'name': info_about.name,
                                                        'id': info_about.id,
                                                        'books': books,
                                                        'num': len(books),
                                                        'min': round(price['min'], 3),
                                                        'max': round(price['max'], 3),
                                                        })


def books(request):
    books = Book.objects.all().annotate(authors_count=Count('authors'))

    return render(request, 'mysite/books.html', {'books': books})


def book_detail(request, pk):
    book = Book.objects.get(id=pk)

    queryset_publisher = Book.objects.select_related('publisher').get(id=pk)

    queryset_stores = Store.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.filter(id=pk)))

    stores = []
    for store in queryset_stores:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})

    authors = Author.objects.filter(book__id=pk)

    return render(request, 'mysite/book_detail.html', {'id': book.id,
                                                       'name': book.name,
                                                       'pages': book.pages,
                                                       'price': book.price,
                                                       'rating': book.rating,
                                                       'publisher': queryset_publisher.publisher,
                                                       'authors': authors,
                                                       'pubdate': book.pubdate,
                                                       'stores': stores})
