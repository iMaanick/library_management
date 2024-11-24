from click import Group

from app.cli.commands import add, delete, search, update_status, list_books


def init_commands(app: Group) -> None:
    app.add_command(add, name="add")
    app.add_command(delete, name="delete")
    app.add_command(search, name="search")
    app.add_command(update_status, name="update_status")
    app.add_command(list_books, name="list_books")
