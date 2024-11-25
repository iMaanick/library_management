from typing import Optional

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from app.application.models import Book, BookStatus
from app.application.protocols import BookDatabaseGateway
from app.adapters.sqlalchemy_db import models


class BookSqlGateway(BookDatabaseGateway):
    def __init__(self, db_uri: str):
        self.engine = create_engine(db_uri, echo=False)
        self.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def add_book(self, title: str, author: str, year: int) -> Book:
        with self.session_maker() as session:
            book = models.Book(title=title, author=author, year=year)
            session.add(book)
            session.commit()
            session.refresh(book)
            return book.to_dto()

    def delete_book(self, book_id: int) -> Optional[Book]:
        with self.session_maker() as session:
            query = select(models.Book).where(models.Book.id == book_id)
            book = session.execute(query).scalars().first()
            if book:
                session.delete(book)
                session.commit()
                return book.to_dto()
            return None

    def search_books(
            self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None
    ) -> list[Book]:
        with self.session_maker() as session:
            query = select(models.Book)
            if title:
                query = query.filter(models.Book.title.ilike(f"%{title}%"))
            if author:
                query = query.filter(models.Book.author.ilike(f"%{author}%"))
            if year:
                query = query.filter(models.Book.year == year)

            result = session.execute(query).scalars().all()
            books = [book.to_dto() for book in result]
            return books

    def update_book_status(self, book_id: int, status: BookStatus) -> Optional[Book]:
        with self.session_maker() as session:
            query = select(models.Book).where(models.Book.id == book_id)
            result = session.execute(query).scalars().first()
            if result:
                result.status = models.BookStatus(status)
                session.commit()
                session.refresh(result)
                return result.to_dto()

            return None

    def get_all_books(self) -> list[Book]:
        with self.session_maker() as session:
            result = session.execute(select(models.Book)).scalars().all()
            books = [book.to_dto() for book in result]
            return books
