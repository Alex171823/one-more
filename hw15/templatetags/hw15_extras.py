from random import randint

from better_profanity import profanity

from django import template

from mysite.models import Book

register = template.Library()


# returns random book and it's publisher as a string
@register.simple_tag
def random_book_publisher():
    random = randint(1, Book.objects.all().count())
    queryset = Book.objects.filter(id=random)
    for book in queryset:
        result = "book name: " + book.name + " , publisher name: " + str(book.publisher)
        return result


# returns censored phrase, changing profanity word as ***
@register.filter(name="clear_phrase")
def clear_phrase(value):
    return profanity.censor(value)
