import strawberry
from .models import Book


@strawberry.django.type(Book)
class BookType:
    name: str
    author: str
