from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    user_id: int
    account_creation_date: datetime
    role: Optional[int]

    class Config:
        orm_mode = True
