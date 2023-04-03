from pydantic import BaseModel
from fastapi import Response, HTTPException

from adapters.driving import http_auth_api
from domain.errors import UserError, PasswordDoesNotMatch
from domain.value_objects import Username, PlainPassword, SessionId


class Credentials(BaseModel):
    username: str
    password: str

    @classmethod
    def split(cls, credentials):
        return Username(credentials.username), PlainPassword(credentials.password)


async def login_action(credentials: Credentials, response: Response) -> SessionId:
    try:
        username, password = Credentials.split(credentials)
        session_id = await http_auth_api.login(username, password)

        response.set_cookie('session_id', session_id.raw())
        return session_id
    except (UserError, PasswordDoesNotMatch):
        raise HTTPException(status_code=401, detail='Invalid credentials')
