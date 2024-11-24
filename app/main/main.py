from dotenv import load_dotenv

from app.cli.commands import cli
from app.main.setup import setup

if __name__ == "__main__":
    load_dotenv()
    setup(cli)
