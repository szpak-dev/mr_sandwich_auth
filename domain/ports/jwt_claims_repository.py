from abc import abstractmethod

from domain.auth import JwtClaims
from domain.entities import User
from shared.ddd import BaseRepository
from domain.value_objects import SessionId


class JwtClaimsRepository(BaseRepository):
    @abstractmethod
    def get_by_session_id(self, session_id: SessionId) -> JwtClaims:
        pass

    @abstractmethod
    def save(self, session_id: SessionId, user: User) -> None:
        pass
