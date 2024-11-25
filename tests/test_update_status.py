import click
from click.testing import CliRunner


def test_update_status_valid(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "update_status 1 'выдана'")
    assert result.exit_code == 0
    assert "Updated status for book ID 1 to выдана" in result.output


def test_update_status_invalid_id(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "update_status invalid_id 'в наличии'")
    assert result.exit_code == 2
    assert "Error: Invalid value for 'BOOK_ID': 'invalid_id' is not a valid integer." in result.output


def test_update_status_invalid_status(runner: CliRunner, test_cli: click.Group) -> None:
    result = runner.invoke(test_cli, "update_status 1 'not_a_status'")
    assert result.exit_code == 2
    assert "Error: Invalid value for '{в наличии|выдана}': 'not_a_status'" in result.output
