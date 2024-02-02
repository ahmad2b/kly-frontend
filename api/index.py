from fastapi import FastAPI, status, HTTPException, Depends
from starlette.responses import JSONResponse, RedirectResponse

from api._public import api as public_api
from api._utils.errors import NotFound
from api._public.url import url_service
from api.config import settings
from api._utils.logger import logger_config

from api.database import get_session
from api._auth import get_current_user
from sqlmodel import Session

logger = logger_config(__name__)

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    contact={
        "name": "Kly.lol",
        "url": "https://www.kly.lol",
        "email": "ahmadshaukat_4@outlook.com",
    },
    servers=[
        # {
        #     "url": "https://www.kly.lol",
        #     "description": "Production server",
        # },
        {
            "url": "https://welcomed-teal-perfectly.ngrok-free.app",
            "description": "Development server",
        },
        {"url": "http://localhost:8000", "description": "Local Development server"},
    ],
    debug=True,
)

app.include_router(public_api)


# API status
@app.get(
    "/api/status",
    tags=["Status"],
    summary="Status of API",
    description="Status of API",
    responses={
        200: {
            "description": "Status of API",
            "content": {"application/json": {"example": {"status": "UP"}}},
        }
    },
)
def api_status():
    return JSONResponse({"status": "UP"})


# Redirect API
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
async def redirect(short_url: str, db: Session = Depends(get_session)):
    try:
        url = url_service.get_url(short_url, db=db)
        if not url:
            raise NotFound(f"URL with short URL {short_url} not found")
        return RedirectResponse(url.url)
    except NotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, reload=True)
