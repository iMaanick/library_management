from typing import Callable, Any

import click

from app.main.commands import init_commands


def setup(app: Callable[..., Any]) -> None:
    app = click.pass_context(app)
    app = click.group(app)
    init_commands(app)
    app()
