from typing import Annotated

from fastapi import FastAPI, Header, HTTPException
import re

app = FastAPI()


@app.get('/headers')
async def get_headers(user_agent: Annotated[str | None, Header()] = None,
                      accept_language: Annotated[str | None, Header()] = None):

    if not user_agent or not accept_language:
        raise HTTPException(
            status_code=400, detail='Required headers are missing')

    if not re.search(
            r'.{2}-.{2},.{2};q=0\.\d,(.{2}|.{2}-.{2});q=0\.\d($|,.{2};q=0\.\d)', accept_language):
        return HTTPException(400, 'Invalid Accept-Language format')

    return {'User-Agent': user_agent, 'Accept-Language': accept_language}
