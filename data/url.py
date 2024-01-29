from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from schema.url import URLCreate, URLInDB, URL as URLSchema
from errors import Missing, Duplicate

from typing import Optional

from model.url import URL


def create_url(db: Session, url: URLCreate, short_url: str) -> URLInDB:
    db_url = URL(
        original_url=str(url.original_url),
        short_url=short_url,
        custom_alias=url.custom_alias,
        description=url.description,
    )
    try:
        db.add(db_url)
        db.commit()
        db.refresh(db_url)
        return db_url
    except IntegrityError:
        db.rollback()
        raise Duplicate("Short Url already exists")
    except Exception as e:
        db.rollback()
        raise e
    return db_url


def get_url(db: Session, short_url: str) -> Optional[URLInDB]:
    url = db.query(URL).filter(URL.short_url == short_url).first()
    return url


# def update_url(db: Session, url: URL):
#     try:
#         db.query(URL).filter(URL.id == url.id).update({URL: url})
#         db.commit()
#     except IntegrityError:
#         db.rollback()
#         raise ValueError(f"Update {url.short_url} failed")
#     return db.query(URL).filter(URL.id == url.id).first()


# def delete_url(db: Session, short_url: str):
#     try:
#         db.query(URL).filter(URL.short_url == short_url).delete()
#         db.commit()
#     except IntegrityError:
#         db.rollback()
#         raise ValueError(f"Delete {short_url} failed")
