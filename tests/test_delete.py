def test_delete_book(runner, test_cli):
    result = runner.invoke(test_cli, "delete 1")
    assert result.exit_code == 0
    assert "Deleted book Test Book with ID: 1" in result.output


def test_delete_book_invalid_id(runner, test_cli):
    result = runner.invoke(test_cli, "delete invalid_id")
    assert result.exit_code == 2
    assert "Error: Invalid value for 'BOOK_ID': 'invalid_id' is not a valid integer." in result.output


def test_delete_book_non_existent_id(runner, test_cli):
    result = runner.invoke(test_cli, "delete 9999")
    assert result.exit_code == 0
    assert "Error: Book with ID 9999 not found." in result.output

