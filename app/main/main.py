from dotenv import load_dotenv

from app.cli.commands import main

if __name__ == "__main__":
    load_dotenv()
    main()