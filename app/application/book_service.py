from app.application.models import Book, BookStatus
from app.application.protocols import BookDatabaseGateway


class BookService:
    def __init__(self, db: BookDatabaseGateway):
        self.db = db

    def add_book(self, title: str, author: str, year: int) -> Book:
        return self.db.add_book(title, author, year)

    def delete_book(self, book_id: int) -> Book:
        book = self.db.delete_book(book_id)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")
        return book

    def search_books(self, title: str = None, author: str = None, year: int = None):
        return self.db.search_books(title, author, year)

    def update_book_status(self, book_id: int, status: BookStatus):
        book = self.db.update_book_status(book_id, status)
        if not book:
            raise ValueError(f"Book with ID {book_id} not found.")
        return book

    def get_books(self):
        return self.db.get_all_books()