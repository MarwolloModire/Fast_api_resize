from pydantic import BaseModel, constr


class User(BaseModel):
    username: str
    password: constr(min_length=8, max_length=20)
