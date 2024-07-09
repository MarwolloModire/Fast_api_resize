from fastapi import FastAPI
from models.models import User


app = FastAPI()
user = User(name='Jonny Kage', age=42)


@app.get("/users")
def get_all_users():
    return {
        "name": user.name,
        "age": user.age
    }


@app.post('/user')
async def post_user_data(user: User) -> User:
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": user.age >= 18
    }
