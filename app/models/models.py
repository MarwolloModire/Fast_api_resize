from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


# добавим симуляцию базы данных в виде массива объектов юзеров
USER_DATA = [User(**{"username": "user1", "password": "pass1"}),
             User(**{"username": "user2", "password": "pass2"})]
