from pydantic import BaseModel
from typing import Optional
from enum import Enum


class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"
    guest = "guest"


class RoleBase(BaseModel):
    role_name: RoleEnum
    permissions: Optional[str]


class RoleCreate(RoleBase):
    pass


class RoleResponse(RoleBase):
    role_id: int

    class Config:
        orm_mode = True


class UserRoleBase(BaseModel):
    user_id: int
    role_id: int


class UserRoleCreate(UserRoleBase):
    pass


class UserRoleResponse(UserRoleBase):
    class Config:
        orm_mode = True
