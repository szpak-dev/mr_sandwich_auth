from domain.entities import User
from domain.errors import UserAlreadyExists, UserNotFound
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, PlainPassword, UserId


class HttpUserApi:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def create_user(self, username: Username, plain_password: PlainPassword) -> None:
        try:
            await self._user_repository.get_by_username(username)
            raise UserAlreadyExists
        except UserNotFound:
            user = User()
            user.username = username.value
            user.password = plain_password.encode().encoded

            await self._user_repository.save(user)

    def get_user(self, user_id: UserId):
        pass
