from fastapi import FastAPI, Depends, status, HTTPException, Request
from starlette.responses import JSONResponse, RedirectResponse

from typing import Annotated

from .models import URL
from .service import get_url, create_url
from .errors import NotFound, Duplicate


app = FastAPI(
    # docs_url="/api/docs/",
    # openapi_url="/api/openapi.json/",
    title="Kly.lol API Docs",
    description="Kly.lol is a URL shortener service powered by Gemini with FastAPI and Next.js.",
    version="0.1.0",
    contact={
        "name": "Kly.lol",
        "url": "https://www.kly.lol",
        "email": "ahmadshaukat_4@outlook.com",
    },
    servers=[
        {
            "url": "https://www.kly.lol",
            "description": "Production server",
        },
        {"url": "http://localhost:8000", "description": "Local Development server"},
    ],
    debug=True,
)


@app.get(
    "/api",
)
async def root():
    return {"message": "Hello World"}


@app.get(
    "/api/{short_url}",
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
async def redirect(short_url: str):
    try:
        url = get_url(short_url)
        if not url:
            raise NotFound(f"URL with short URL {short_url} not found")
        return RedirectResponse(url.original_url)
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post(
    "/api/url",
    tags=["URL"],
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
async def create(url: URL) -> URL:
    try:
        return create_url(url)
    except Duplicate as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/api/url/{short_url}",
    tags=["URL"],
)
async def get_original_url(short_url):
    try:
        url = get_url(short_url)
        return url.url
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, reload=True)
