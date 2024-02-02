from fastapi.testclient import TestClient
from fastapi import status, HTTPException
from sqlalchemy.exc import IntegrityError

from model.url import URL
from schema.url import URLCreate, URLInDB, URL as URLSchema

from service import url as service
from data.init import get_db
from main import app


client = TestClient(app)


def test_create_url_success():
    url = URLCreate(
        original_url="https://www.example.com",
    )

    body = {"original_url": "https://www.example.com"}

    result = client.post("/api/url", json=body)
    result_json = result.json()
    print(result_json)
    assert result.status_code == status.HTTP_201_CREATED
    # assert result_json["original_url"] == body.original_url


# def test_create_url_success():
#     # Arrange
#     db = Mock()
#     db_url = URL(
#         original_url="http://example.com",
#         short_url="short",
#         custom_alias="alias",
#         description="description",
#     )
#     url_create = URLCreate(
#         original_url="http://example.com",
#         custom_alias="alias",
#         description="description",
#     )

#     # Act
#     result = create_url(db, url_create, "short")

#     # Assert
#     db.add.assert_called_once_with(db_url)
#     db.commit.assert_called_once()
#     db.refresh.assert_called_once_with(db_url)
#     assert result == db_url

# def test_create_url_duplicate():
#     # Arrange
#     db = Mock()
#     db.add.side_effect = IntegrityError(None, None, None)
#     url_create = URLCreate(
#         original_url="http://example.com",
#         custom_alias="alias",
#         description="description",
#     )

#     # Act & Assert
#     with pytest.raises(Duplicate):
#         create_url(db, url_create, "short")

# def test_create_url_exception():
#     # Arrange
#     db = Mock()
#     db.add.side_effect = Exception("Test exception")
#     url_create = URLCreate(
#         original_url="http://example.com",
#         custom_alias="alias",
#         description="description",
#     )

#     # Act & Assert
#     with pytest.raises(Exception):
#         create_url(db, url_create, "short")
