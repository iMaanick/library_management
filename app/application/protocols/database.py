from abc import ABC, abstractmethod
from typing import Optional

from app.application.models import Book, BookStatus


class BookDatabaseGateway(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int) -> Book:
        raise NotImplementedError

    @abstractmethod
    def delete_book(self, book_id: int) -> Optional[Book]:
        raise NotImplementedError

    @abstractmethod
    def search_books(
            self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None
    ) -> list[Book]:
        raise NotImplementedError

    @abstractmethod
    def update_book_status(self, book_id: int, status: BookStatus) -> Optional[Book]:
        raise NotImplementedError

    @abstractmethod
    def get_all_books(self) -> list[Book]:
        raise NotImplementedError
