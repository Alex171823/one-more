from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.age}"


class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.pages} {self.price} {self.rating} {self.publisher} {self.pubdate}"

    def get_absolute_url(self):
        return reverse('update-book', kwargs={'pk': self.pk})


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f"{self.name} {self.books}"


# class AuthorBookManyToMany(models.Model):
#     book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
#     author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
#     time_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.book_id} {self.book_id} {self.time_created}"
