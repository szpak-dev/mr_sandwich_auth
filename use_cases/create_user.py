from pydantic import BaseModel
from fastapi import HTTPException

from adapters.driving import http_user_api
from domain.errors import UserAlreadyExists
from domain.value_objects import Username, PlainPassword


class Registration(BaseModel):
    username: str
    password: str
    repeat_password: str

    @classmethod
    def split(cls, registration):
        return Username(registration.username), PlainPassword(registration.password)


async def create_user_action(registration: Registration) -> None:
    username, password = Registration.split(registration)

    try:
        await http_user_api.create_user(username, password)
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))
