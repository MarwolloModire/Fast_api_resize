from fastapi import FastAPI, Response, Cookie
from fastapi.responses import JSONResponse
from secrets import token_urlsafe
from models.models import User

app = FastAPI()


arr = (('Patrick', 'Superstar'),
       ('Bob', 'Crastysponge'),
       ('user345', 'password345'))
cookie_dict = {}


@app.post('/login')
async def create_cookie(user: User):
    if (user.username, user.password) in arr:
        cookie_dict[ck_name := 'session_token'] = (
            token := token_urlsafe(16)), user
        response = JSONResponse(content={"message": "Login successful"})
        response.set_cookie(key=ck_name, value=token,
                            max_age=60, secure=True, httponly=True)
        return response
    return JSONResponse(content={"message": "User not found, please try again!"})


@app.get('/user')
async def read_items(session_token: str | None = Cookie(default=None)):
    if session_token \
            and (items := cookie_dict.get('session_token', None))\
            and session_token == items[0]:
        return items[1]
    return JSONResponse(content={'message': 'Unauthorized'})


@app.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('session_token')
