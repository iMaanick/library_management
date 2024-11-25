import click
from dishka import FromDishka, make_container
from dishka.integrations.click import setup_dishka

from app.application.book_service import BookService
from app.application.commands import validate_year, add_book, delete_book, search_books, update_book_status, get_books
from app.application.models import BookStatus
from app.main.di import AdaptersProvider, ServiceProvider


def cli(context: click.Context):
    container = make_container(AdaptersProvider(), ServiceProvider())
    setup_dishka(container=container, context=context, auto_inject=True)


@click.command()
@click.argument("title")
@click.argument("author")
@click.argument("year", type=int)
def add(title: str, author: str, year: int, book_service: FromDishka[BookService]):
    try:
        validate_year(year)
    except ValueError as e:
        click.echo(click.style("Error: ", fg="red") + f"{e}")
        return
    book = add_book(title, author, year, book_service)
    click.echo(f"Added book {book.title} with ID: {book.id}")


@click.command()
@click.argument("book_id", type=int)
def delete(book_id: int, book_service: FromDishka[BookService]):
    try:
        book = delete_book(book_id, book_service)
        click.echo(f"Deleted book {book.title} with ID: {book.id}")
    except ValueError as e:
        click.echo(click.style("Error: ", fg="red") + f"{e}")


@click.command()
@click.option("--title", default=None, help="Search by title")
@click.option("--author", default=None, help="Search by author")
@click.option("--year", default=None, type=int, help="Search by year")
def search(title: str, author: str, year: int, book_service: FromDishka[BookService]):
    try:
        validate_year(year)
    except ValueError as e:
        click.echo(click.style("Error: ", fg="red") + f"{e}")
        return
    books = search_books(title, author, year, book_service)
    if not books:
        click.echo("No books found")
        return
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, "
                   f"Year: {book.year}, Status: {book.status.value}")


@click.command()
@click.argument("book_id", type=int)
@click.argument("status", type=click.Choice(["в наличии", "выдана"]))
def update_status(book_id: int, status: str, book_service: FromDishka[BookService]):
    try:
        book = update_book_status(book_id, BookStatus(status), book_service)
        click.echo(f"Updated status for book ID {book.id} to {book.status}")
    except ValueError as e:
        click.echo(click.style("Error: ", fg="red") + f"{e}")


@click.command()
def list_books(book_service: FromDishka[BookService]):
    books = get_books(book_service)
    if not books:
        click.echo("No books found in the library.")
        return
    click.echo("Books in the library:")
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, "
                   f"Year: {book.year}, Status: {book.status.value}")
