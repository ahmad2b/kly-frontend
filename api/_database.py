from sqlmodel import Field, SQLModel, create_engine

from .config import settings
from .models import URL, User

database_url = settings.database_url

engine = create_engine(database_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine, tables=[URL.__table__, User.__table__])


if __name__ == "__main__":
    create_db_and_tables()
