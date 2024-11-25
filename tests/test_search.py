import click
from click.testing import CliRunner


def test_search_books_no_filters(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "search")
    assert result.exit_code == 0
    assert "ID: 1, Title: Test Book, Author: Test Author, Year: 2024, Status: в наличии" in result.output


def test_search_books_with_title(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'search --title "Test Book"')
    assert result.exit_code == 0
    assert "ID: 1, Title: Test Book, Author: Test Author, Year: 2024, Status: в наличии" in result.output


def test_search_books_with_invalid_year(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "search --year 2024.5")
    assert result.exit_code == 2
    assert "Error: Invalid value for '--year': '2024.5' is not a valid integer." in result.output


def test_search_books_no_results(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'search --title "Nonexistent Book"')
    assert result.exit_code == 0
    assert "No books found" in result.output
