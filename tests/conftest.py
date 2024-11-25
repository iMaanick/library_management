from typing import Optional

import click
import pytest
from click.testing import CliRunner
from dishka import make_container, provide, Scope, Provider
from dishka.integrations.click import setup_dishka

from app.application.models import Book, BookStatus
from app.application.protocols import BookDatabaseGateway
from app.main.commands import init_commands
from app.main.di import ServiceProvider


class BookTestGateway(BookDatabaseGateway):
    def add_book(self, title: str, author: str, year: int) -> Book:
        return Book(
            id=1,
            title=title,
            author=author,
            year=year
        )

    def delete_book(self, book_id: int) -> Optional[Book]:
        if book_id == 1:
            return Book(
                id=1,
                title="Test Book",
                author="Test Author",
                year=2024
            )
        return None

    def search_books(
            self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None
    ) -> list[Book]:
        if title == "Test Book" or all(field is None for field in [title, author, year]):
            return [Book(
                id=1,
                title="Test Book",
                author="Test Author",
                year=2024
            )]
        return []

    def update_book_status(self, book_id: int, status: BookStatus) -> Optional[Book]:
        if book_id == 1:
            return Book(
                id=1,
                title="Test Book",
                author="Test Author",
                year=2024,
                status=BookStatus.ISSUED
            )
        return None

    def get_all_books(self) -> list[Book]:
        return [Book(
            id=1,
            title="Test Book",
            author="Test Author",
            year=2024
        )]


class TestAdaptersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_db(self) -> BookDatabaseGateway:
        return BookTestGateway()


def cli(context: click.Context) -> None:
    container = make_container(TestAdaptersProvider(), ServiceProvider())
    setup_dishka(container=container, context=context, auto_inject=True)


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def test_cli() -> click.Group:
    test_cli = cli
    test_cli = click.pass_context(test_cli)
    test_cli = click.group(test_cli)
    init_commands(test_cli)
    return test_cli
