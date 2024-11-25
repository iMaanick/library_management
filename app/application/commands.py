from app.application.book_service import BookService
from app.application.models import Book, BookStatus


def validate_year(year: int) -> None:
    if year and year < 0:
        raise ValueError(f"Year must be a non-negative integer.")


def add_book(title: str, author: str, year: int, book_service: BookService) -> Book:
    return book_service.add_book(title, author, year)


def delete_book(book_id: int, book_service: BookService) -> Book:
    return book_service.delete_book(book_id)


def search_books(title: str, author: str, year: int, book_service: BookService) -> list[Book]:
    return book_service.search_books(title, author, year)


def update_book_status(book_id: int, status: BookStatus, book_service: BookService) -> Book:
    return book_service.update_book_status(book_id, status)


def get_books(book_service: BookService) -> list[Book]:
    return book_service.get_books()
