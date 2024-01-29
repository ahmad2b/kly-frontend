from datetime import datetime
from typing import Union, Optional
from pydantic import BaseModel, HttpUrl, validator


class URLCreate(BaseModel):
    original_url: HttpUrl
    custom_alias: Union[str | None] = None
    description: Union[str | None] = None

    @validator("original_url")
    def validate_original_url(cls, v):
        if "localhost" in str(v):
            raise ValueError("localhost URLs are not allowed")
        return v


class URL(URLCreate):
    short_url: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    expiration_date: Optional[datetime]

    class Config:
        orm_mode = True


class URLInDB(URL):
    id: Optional[int]
    access_count: int
