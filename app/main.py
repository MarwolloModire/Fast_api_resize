from fastapi import FastAPI, status
from models.models import UserCreate


app = FastAPI()


@app.post('/create_user', status_code=status.HTTP_201_CREATED)
async def transfer_user_data(user: UserCreate) -> UserCreate:
    return user
