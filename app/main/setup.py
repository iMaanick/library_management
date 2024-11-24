from typing import Callable

import click

from app.main.commands import init_commands


def setup(app: Callable) -> None:
    app = click.pass_context(app)
    app = click.group(app)
    init_commands(app)
    app()
