from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None = Field(default=None, gt=0)
    is_subscribed: bool | None = None
