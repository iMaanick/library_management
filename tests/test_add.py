import click
from click.testing import CliRunner


def test_add_book(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'add "Test Book" "Test Author" 2024')
    assert result.exit_code == 0
    assert "Added book Test Book with ID: 1" in result.output


def test_add_book_incorrect_year(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'add "Test Book" "Test Author" 2024.5')
    assert result.exit_code == 2
    assert "Error: Invalid value for 'YEAR': '2024.5' is not a valid integer." in result.output


def test_add_book_negative_year(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'add "Test Book" "Test Author" -- -2024')
    assert result.exit_code == 0
    assert "Error: Year must be a non-negative integer." in result.output


def test_add_book_no_such_option(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, 'add "Test Book" "Test Author" -2024')
    assert result.exit_code == 2
    assert "Error: No such option: -2" in result.output
