from fastapi import APIRouter, Depends

from api._public.user import views as user
from api._public.url import views as url

api = APIRouter()


api.include_router(
    user.router,
    prefix="/api/users",
    tags=["User"],
    # dependencies=[Depends(authent)],
)


api.include_router(
    url.router,
    prefix="/api/url",
    tags=["URL"],
    # dependencies=[Depends(authent)],
)
