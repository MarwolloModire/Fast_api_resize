from pydantic import BaseModel


# создаём модель данных, которая обычно расположена в файле models.py
class User(BaseModel):
    name: str
    age: int
    is_adult: bool | None = None
