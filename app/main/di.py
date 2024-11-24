import os

from dishka import Provider, provide, Scope

from app.adapters.sqlalchemy_db.gateway import BookSqlGateway
from app.application.book_service import BookService
from app.application.protocols import BookDatabaseGateway


class AdaptersProvider(Provider):
    @provide(scope=Scope.APP)
    def get_db(self) -> BookDatabaseGateway:
        db_uri = os.getenv('DATABASE_URI')
        if not db_uri:
            raise ValueError("DB_URI env variable is not set")
        return BookSqlGateway(db_uri)


class ServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_book_service(self, db: BookDatabaseGateway) -> BookService:
        return BookService(db)
