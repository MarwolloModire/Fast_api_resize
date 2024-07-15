from datetime import datetime, timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.models import User
from secrets import token_urlsafe
from passlib.context import CryptContext
import jwt


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = token_urlsafe(16)
ALGORITHM = 'HS256'
# Устанавливаем 'время жизни' токена
EXPIRATION_TIME = timedelta(minutes=1)
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

USERS_DATA = [
    {'username': 'john_doe', 'password': 'securepassword123'}
]
# Хэшируем пароли в ДБ
for h_p in USERS_DATA:
    h_p['password'] = pwd_context.hash(h_p['password'])


# Функция создания токена с применением времени сгорания
def create_jwt_token(data: dict):
    data.update({'exp': datetime.utcnow() + EXPIRATION_TIME})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


# Функция проверки пользователя (Аутентификация)
def authenticate_user(username: str, password: str):
    for user in USERS_DATA:
        if user['username'] == username:
            return pwd_context.verify(password, user['password'])
    return False


# Функция для проверки токена
def verify_jwt_token(token: str = Depends(oauth2_scheme)):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='The token has expired')
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail='Invalid token')


# Роут для входа
@app.post('/login')
async def login(user_in: User):
    if authenticate_user(user_in.username, user_in.password):
        return {'access_token': create_jwt_token({'sub': user_in.username}), 'token_type': 'bearer'}
    raise HTTPException(status_code=401, detail='Invalid credentials')


# Защищенный роут для получения информации о доступе
@app.get('/protected_resource')
async def about_me(verified_user: dict = Depends(verify_jwt_token)):
    if verified_user:
        return {'message': "Access granted! Let's GOOO!"}
