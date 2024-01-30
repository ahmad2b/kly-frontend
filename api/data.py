from sqlmodel import Session, select
from ._database import engine
from .models import URL, User

from typing import Optional


def create(url: URL) -> URL:
    with Session(engine) as session:
        session.add(url)
        session.commit()
        session.refresh(url)
        return url


def get_by_short_url(short_url: str) -> Optional[URL]:
    with Session(engine) as session:
        statement = select(URL).where(URL.short_url == short_url)
        result = session.exec(statement).first()
        return result
