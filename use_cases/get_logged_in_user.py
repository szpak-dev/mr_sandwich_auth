from fastapi import Request, HTTPException
from pydantic import BaseModel

from adapters.driving import http_auth_api
from domain.errors import IdentityNotFound, SessionNotFound, UserNotFound
from domain.services import extract_session_id


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


async def get_logged_in_user_action(request: Request) -> User:
    try:
        session_id = extract_session_id(request)
        return await http_auth_api.get_logged_in_user(session_id)
    except (IdentityNotFound, SessionNotFound, UserNotFound) as e:
        raise HTTPException(status_code=401, detail=str(e))
