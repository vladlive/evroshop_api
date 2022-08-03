from datetime import date
from enum import Enum

from pydantic import BaseModel


class UserPermission(str, Enum):
    ADMIN: str = 'Admin'
    USER: str = 'User'


class UserBase(BaseModel):
    u_name: str
    u_username: str
    u_access: UserPermission
    date: date


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass

