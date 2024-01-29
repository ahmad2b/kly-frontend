from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from data.init import Base

from datetime import datetime
from datetime import timedelta


class User(Base):
    __tablename__ = "Users"
    user_id = Column(
        Integer, primary_key=True, autoincrement=True, index=True, nullable=False
    )
    username = Column(String(255), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    account_creation_date = Column(DateTime, nullable=False, default=datetime.now())
    role = Column(Integer, ForeignKey("Roles.role_id"), default=2)
    urls = relationship("URL", backref="user")
    roles = relationship("UserRole", backref="user")

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
