from pickle import loads, dumps

from domain.auth import JwtClaims
from domain.entities import User
from domain.errors import JwtClaimsNotFound
from domain.ports.jwt_claims_repository import JwtClaimsRepository
from domain.value_objects import SessionId

jwt_claims_by_session_id = {}


class InMemoryJwtClaimsRepository(JwtClaimsRepository):
    def get_by_session_id(self, session_id: SessionId) -> JwtClaims:
        claims = jwt_claims_by_session_id.get(session_id.value)
        if not claims:
            raise JwtClaimsNotFound

        return loads(claims)

    def save(self, session_id: SessionId, user: User) -> None:
        jwt_claims = JwtClaims(user.username, ['ROLE_USER'])
        jwt_claims_by_session_id[session_id.value] = dumps(jwt_claims)
