from domain.entities import User, UserRole
from domain.errors import UserNotFound
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, UserId
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

from shared.async_db import Database


class SqlUserRepository(UserRepository):
    def __init__(self, database: Database):
        self.session = database.current_session()

    async def get_by_id(self, user_id: UserId) -> User:
        user_id = int(user_id.id)
        try:
            result = await self.session.execute(
                select(User)
                .filter(User.id == user_id)
                .join(UserRole, isouter=True)
            )

            return result.scalars().one()
        except NoResultFound:
            raise UserNotFound

    async def get_by_username(self, username: Username) -> User:
        username = username.value
        try:
            result = await self.session.execute(
                select(User)
                .filter(User.username == username)
                .join(UserRole, isouter=True)
            )

            return result.scalars().one()
        except NoResultFound:
            raise UserNotFound

    async def save(self, user: User) -> None:
        self.session.add(user)
        await self.session.commit()
