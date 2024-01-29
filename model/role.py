from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from data.init import Base

from datetime import datetime
from datetime import timedelta


class Role(Base):
    __tablename__ = "Roles"
    role_id = Column(Integer, primary_key=True)
    role_name = Column(String(255))
    permissions = Column(String(255))
    user_roles = relationship("UserRole", backref="role")

    def __repr__(self):
        return f"<Role(role_name={self.role_name}, permissions={self.permissions})>"


class UserRole(Base):
    __tablename__ = "UserRoles"
    user_id = Column(Integer, ForeignKey("Users.user_id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("Roles.role_id"), primary_key=True)

    def __repr__(self):
        return f"<UserRole(user_id={self.user_id}, role_id={self.role_id})>"
