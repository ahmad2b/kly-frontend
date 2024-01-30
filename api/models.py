from typing import List, Optional
from datetime import datetime, timedelta

from sqlmodel import Field, SQLModel, Relationship


class URL(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str = Field(nullable=False, index=True)
    short_url: str = Field(nullable=False, index=True, unique=True)
    clicks: Optional[int] = Field(default=0)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=None)
    expires_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(days=30)
    )
    deleted_at: Optional[datetime] = Field(default_factory=None)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    user: Optional["User"] = Relationship(back_populates="urls")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(nullable=False, index=True, unique=True)
    hash_password: str = Field(nullable=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=None)
    deleted_at: Optional[datetime] = Field(default_factory=None)

    urls: List[URL] = Relationship(back_populates="user")


class UserCreate(SQLModel):
    username: str
    password: str
