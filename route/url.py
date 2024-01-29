from fastapi import APIRouter, HTTPException, status
from schema.url import URLCreate, URL
from service import url as service
from data.init import get_db
from typing import Annotated
from sqlalchemy.orm import Session
from logger import logger
from fastapi import Depends
from starlette.responses import JSONResponse

from errors import Duplicate, Missing

router = APIRouter(
    prefix="/api/url",
    tags=["URL"],
)


@router.post(
    "",
    response_model=URL,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new short URL",
    description="Create a new URL. If description is not provided, the url content will be used to generate relvent alias.",
    responses={
        400: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "URL is missing",
                    }
                }
            }
        },
        409: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "URL already exists",
                    }
                }
            }
        },
        422: {
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid URL",
                    }
                }
            }
        },
    },
    deprecated=False,
)
async def create(db: Annotated[Session, Depends(get_db)], url: URLCreate) -> URL:
    try:
        return service.create(db, url)
    except Duplicate as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{short_url}")
async def get_original_url(db: Annotated[Session, Depends(get_db)], short_url):
    try:
        url = service.get_url(db, short_url)
        return url.original_url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
