import random
import string
from data import url as data
from schema.url import URLCreate, URLInDB, URL
from logger import logger
from sqlalchemy.orm import Session

from service import gemini as service


def smart_url_fn(data: str):
    url = service.shorten_url(data)
    random_chars = "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=3
        )
    )
    return url + "-" + random_chars


def create(db: Session, url: URLCreate):
    smart_url = smart_url_fn(str(url.original_url))
    while data.get_url(db, smart_url):
        smart_url = smart_url_fn(str(url.original_url))
    return data.create_url(db=db, url=url, short_url=smart_url)


# def generate_short_url():
#     """
#     Generate a random string of letters and digits of length 8.
#     Returns:
#         str: A random string of letters and digits of length 8.
#     """
#     return "".join(
#         random.choices(
#             string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8
#         )
#     )


def get_url(db: Session, short_url: str):
    return data.get_url(db, short_url)


# def update(short_url):
#     return data.update_url(short_url)


# def delete(short_url):
#     return data.delete_url(short_url)
