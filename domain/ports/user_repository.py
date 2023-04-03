from abc import abstractmethod

from shared.ddd import BaseRepository
from domain.entities import User
from domain.value_objects import Username, UserId


class UserRepository(BaseRepository):
    @abstractmethod
    async def get_by_id(self, user_id: UserId) -> User:
        pass

    @abstractmethod
    async def get_by_username(self, username: Username) -> User:
        pass

    @abstractmethod
    async def save(self, user: User) -> None:
        pass
