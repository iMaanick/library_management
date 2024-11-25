from typing import Optional

from app.application.models import Book, BookStatus
from app.application.protocols import BookDatabaseGateway


class BookService:
    def __init__(
            self,
            db: BookDatabaseGateway
    ) -> None:
        self.db = db

    def add_book(
            self,
            title: str,
            author: str,
            year: int
    ) -> Book:
        return self.db.add_book(title, author, year)

    def delete_book(
            self,
            book_id: int
    ) -> Book:
        book = self.db.delete_book(book_id)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")
        return book

    def search_books(
            self,
            title: Optional[str] = None,
            author: Optional[str] = None,
            year: Optional[int] = None
    ) -> list[Book]:
        return self.db.search_books(title, author, year)

    def update_book_status(
            self,
            book_id: int,
            status: BookStatus
    ) -> Book:
        book = self.db.update_book_status(book_id, status)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")
        return book

    def get_books(
            self
    ) -> list[Book]:
        return self.db.get_all_books()
