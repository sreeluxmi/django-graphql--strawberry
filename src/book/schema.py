import strawberry
from typing import AsyncGenerator, List
from .types import BookType
from .models import Book
import asyncio
# from .subscription import Subscription


@strawberry.type
class Query:
    @strawberry.field
    def books(self, author: str = None) -> List[BookType]:
        if author:
            books = Book.objects.filter(author=author)
            return list(books)
        return list(Book.objects.all())


@strawberry.type
class Mutation:
    @strawberry.field
    def create_book(self, name: str, author: str) -> BookType:
        book = Book(name=name, author=author)
        book.save()
        return book

    @strawberry.field
    def update_book(self, name: str, author: str) -> BookType:
        book = Book.objects.get(name=name)
        book.name = name
        book.author = author
        book.save()
        return book


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
