from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Max, Min, Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Author, Book, Publisher, Store


def start(request):
    return HttpResponse("StartPage")


"""
Class-based views
"""


class BookDetailView(DetailView):
    model = Book
    template_name = 'mysite/for_class-based_views/book_detail.html'

    # get author for book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_book'] = Author.objects.filter(book__id=self.kwargs['pk'])
        return context


class BookListView(ListView):
    model = Book
    template_name = 'mysite/for_class-based_views/book_list.html'

    # or else
    # "UnorderedObjectListWarning: Pagination may yield inconsistent results with an
    # unordered object_list: <class 'mysite.models.Book'> QuerySet. return self.paginator_class("
    # warning appears, but still works
    ordering = ['id']

    paginate_by = 10


class BookCreateView(LoginRequiredMixin, CreateView):  # LoginRequiredMixin must be at first
    # login if not
    login_url = '/admin/'
    permission_denied_message = 'Nope :)'

    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template_name = 'mysite/for_class-based_views/book_create.html'

    success_url = reverse_lazy('create-book')


class BookUpdateView(UpdateView):
    model = Book
    fields = ['name', 'pages', 'price', 'rating', 'authors', 'publisher', 'pubdate']
    template_name = 'mysite/for_class-based_views/book_update.html'

    # uses get_absolute_url in 'Book' model


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'mysite/for_class-based_views/book_delete.html'

    success_url = reverse_lazy('list-book')


"""
Function-based views
"""


def authors(request):
    authors = Author.objects.all().annotate()

    return render(request, 'mysite/for_function-based_views/authors.html', {'authors': authors})


def author_detail(request, pk):
    info_about = Author.objects.get(id=pk)

    books = Book.objects.filter(authors__id=pk)

    stores = Store.objects.filter(books__authors__id=pk)

    publeshers = Publisher.objects.filter(book__authors=pk).distinct()

    return render(request, 'mysite/for_function-based_views/author_detail.html', {'name': info_about.name,
                                                                                  'age': info_about.age,
                                                                                  'books': books,
                                                                                  'id': info_about.id,
                                                                                  'stores': stores,
                                                                                  'num': len(books),
                                                                                  'publishers': publeshers})


def publisher(request):
    publishers = Publisher.objects.all()

    return render(request, 'mysite/for_function-based_views/publishers.html', {'publishers': publishers})


def publisher_detail(request, pk):
    info_about = Publisher.objects.get(id=pk)

    list_books = Book.objects.filter(publisher_id=pk)

    queryset = Store.objects.prefetch_related(Prefetch('books', queryset=Book.objects.filter(publisher_id=pk)))
    stores = []
    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'name': store.name, 'books': books})
    # stores = Store.objects.filter(books__publisher_id=pk).distinct() - the same

    return render(request, 'mysite/for_function-based_views/publisher_detail.html', {'id': info_about.id,
                                                                                     'name': info_about.name,
                                                                                     'books': list_books,
                                                                                     'num': len(list_books),
                                                                                     'stores': stores,
                                                                                     })


def store(request):
    stores = Store.objects.all()

    return render(request, 'mysite/for_function-based_views/stores.html', {'stores': stores})


def store_detail(request, pk):
    info_about = Store.objects.get(id=pk)

    books = Book.objects.filter(store__id=pk)

    price = Book.objects.filter(store__id=pk).aggregate(max=Max('price'), min=Min('price'))

    return render(request, 'mysite/for_function-based_views/store_detail.html', {'name': info_about.name,
                                                                                 'id': info_about.id,
                                                                                 'books': books,
                                                                                 'num': len(books),
                                                                                 'min': round(price['min'], 3),
                                                                                 'max': round(price['max'], 3),
                                                                                 })


def books(request):
    books = Book.objects.all().annotate(authors_count=Count('authors'))

    return render(request, 'mysite/for_function-based_views/books.html', {'books': books})


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

    return render(request, 'mysite/for_function-based_views/book_detail.html', {'id': book.id,
                                                                                'name': book.name,
                                                                                'pages': book.pages,
                                                                                'price': book.price,
                                                                                'rating': book.rating,
                                                                                'publisher': queryset_publisher.publisher,  # noqa E501
                                                                                'authors': authors,
                                                                                'pubdate': book.pubdate,
                                                                                'stores': stores})
