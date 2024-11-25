from unittest.mock import patch

import click
from click.testing import CliRunner


def test_list_books_with_data(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "list_books")
    assert result.exit_code == 0
    assert "Books in the library:" in result.output
    assert "ID: 1, Title: Test Book, Author: Test Author, Year: 2024, Status: в наличии" in result.output


def test_list_books_no_data(runner: CliRunner, test_cli: click.Group) -> None:
    with patch("app.application.book_service.BookService.get_books", return_value=[]):
        result = runner.invoke(test_cli, "list_books")
        assert result.exit_code == 0
        assert "No books found in the library." in result.output
