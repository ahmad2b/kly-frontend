from fastapi import FastAPI, Depends, HTTPException, status
from route.url import router as url_router

from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from middleware import log_middleware
from starlette.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from data.init import get_db
from typing import Annotated
from logger import logger

from service import url as service

from errors import NotFound

app = FastAPI(
    title="Kly Backend",
    description="Kly.lol a URL shortener with AI powered link management platform built with FastAPI and Next.js",
    version="0.1.0",
    contact={
        "name": "Kly.lol",
        "url": "https://welcomed-teal-perfectly.ngrok-free.app",
        "email": "ahmadshaukat_4@outlook.com",
    },
    servers=[
        {
            "url": "https://welcomed-teal-perfectly.ngrok-free.app",
            "description": "ngRok Development server",
        },
        {"url": "http://localhost:8000", "description": "Local Development server"},
    ],
    debug=True,
)

app.include_router(url_router)


app.add_middleware(
    BaseHTTPMiddleware,
    dispatch=log_middleware,  # type: ignore
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {exc}")
    return JSONResponse({"detail": str(exc.detail)}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


@app.get(
    "/{short_url}",
    response_class=RedirectResponse,
    status_code=status.HTTP_307_TEMPORARY_REDIRECT,
    tags=["Redirect"],
    summary="Redirect to original URL",
    description="Redirect to original URL using short URL",
    responses={
        307: {
            "description": "Redirect to original URL",
        },
        400: {
            "description": "Bad Request",
        },
        404: {
            "description": "URL not found",
        },
    },
    deprecated=False,
)
async def redirect(short_url: str, db: Annotated[Session, Depends(get_db)]):
    try:
        url = service.get_url(db, short_url)
        if not url:
            raise NotFound(f"URL with short URL {short_url} not found")
        return RedirectResponse(url.original_url)
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
