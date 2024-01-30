import random
import string
from .gemini import shorten_url
from .data import create, get_by_short_url
from .models import URL, UserCreate


def smart_url_generator(url: str) -> str:
    """
    Generates a smart URL for the given URL.
    """
    url = shorten_url(url)
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=3))

    return url + "-" + random_string


def create_url(user_url: URL) -> URL:
    """
    Creates a new URL.
    """
    url = smart_url_generator(str(user_url.url))
    while get_by_short_url(url):
        url = smart_url_generator(str(user_url.url))
    return create(URL(url=url, short_url=url, user_id=user_url.user_id))


def get_url(url: str):
    """
    Gets a URL by its short URL.
    """

    return get_by_short_url(url)
