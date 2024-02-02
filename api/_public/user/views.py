from fastapi import APIRouter, Depends, status, HTTPException, status
from api._public.user.models import UserCreate, User
from api._public.user import user_service
from api._utils.errors import (
    HTTPError,
    BadRequest,
    NotFound,
    Unauthorized,
    Forbidden,
    UnprocessableEntity,
    OK,
)
from api._utils.logger import logger_config
from sqlmodel import Session
from api.database import get_session

router = APIRouter()
logger = logger_config(__name__)


@router.post(
    "",
    tags=["User"],
    status_code=status.HTTP_201_CREATED,
    response_model=User,
)
async def create_user(user: UserCreate, db: Session = Depends(get_session)):
    logger.info("%s.create_user: %s", __name__, user)
    try:
        res = user_service.create(db, user)
    except BadRequest as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request {e}"
        )
    except Unauthorized as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized {e}"
        )
    except Forbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Forbidden {e}"
        )
    except NotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Not Found {e}"
        )
    except UnprocessableEntity as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unprocessable Entity {e}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error {e}",
        )
    return res


@router.post("/signin", tags=["User"])
async def login(user: UserCreate, db: Session = Depends(get_session)):
    logger.info("%s.sign_in: %s", __name__, user)
    try:
        response = user_service.sign_in(db, user)
    except BadRequest as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Bad Request {e}"
        )
    except Unauthorized as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Unauthorized {e}"
        )
    except Forbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Forbidden {e}"
        )
    except NotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Not Found {e}"
        )
    except UnprocessableEntity as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Unprocessable Entity {e}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error {e}",
        )
    # response.set_cookie(key="token", value=response.jwt)
    return response
