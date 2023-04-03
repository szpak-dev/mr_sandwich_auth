from domain.ports.jwt_claims_repository import JwtClaimsRepository
from domain.ports.session_repository import SessionRepository
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, PlainPassword, SessionId


class HttpAuthApi:
    def __init__(self,
                 session_repository: SessionRepository,
                 user_repository: UserRepository,
                 jwt_claims_repository: JwtClaimsRepository
                 ):
        self._session_repository = session_repository
        self._user_repository = user_repository
        self._jwt_claims_repository = jwt_claims_repository

    async def login(self, username: Username, plain_password: PlainPassword) -> SessionId:
        user = await self._user_repository.get_by_username(username)
        user.check_password(plain_password)

        session = self._session_repository.create_session(user.get_id())
        self._jwt_claims_repository.save(session.id, user)

        return session.id

    def logout(self, session_id: SessionId):
        self._session_repository.destroy_session(session_id)

    async def get_logged_in_user(self, session_id: SessionId):
        session = self._session_repository.get_by_id(session_id)
        return await self._user_repository.get_by_id(session.user_id)
