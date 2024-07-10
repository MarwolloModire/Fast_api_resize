from pydantic import BaseModel


class Feedback(BaseModel):
    name: str
    message: str


class ResponseModel(BaseModel):
    message: str
