from pydantic import BaseModel
from enum import Enum


class Role(Enum):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'


class Permission(Enum):
    ADMIN = 'create, read, update, delete'
    USER = 'read, update'
    GUEST = 'read'


class UserSchema(BaseModel):
    username: str
    password: str
    role: Role | None = None
    permission: Permission | None = None
