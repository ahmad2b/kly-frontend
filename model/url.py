from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from datetime import timedelta

from data.init import Base


class URL(Base):
    __tablename__ = "urls"
    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    original_url = Column(String(2048), nullable=False, index=True)
    short_url = Column(String(255), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    expiration_date = Column(
        DateTime(timezone=True),
        nullable=True,
        index=True,
        default=func.now() + timedelta(days=30),
    )
    custom_alias = Column(String(255), unique=True, index=True)
    description = Column(String(2048))
    access_count = Column(Integer, nullable=False, default=0)  # New field

    def __repr__(self):
        return f"<URL(original_url={self.original_url}, short_url={self.short_url})>"
