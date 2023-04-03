from domain.auth import JwtClaims
from domain.ports.jwt_claims_repository import JwtClaimsRepository
from domain.ports.session_repository import SessionRepository
from domain.value_objects import SessionId
from domain.services import encode_jwt


class HttpProxyPass:
    def __init__(self, session_repository: SessionRepository, jwt_claims_repository: JwtClaimsRepository):
        self._session_repository = session_repository
        self._jwt_claims_repository = jwt_claims_repository

    def authenticate(self, session_id: SessionId) -> JwtClaims:
        session = self._session_repository.get_by_id(session_id)
        return self._jwt_claims_repository.get_by_session_id(session.id)

    def append_jwt_to_headers(self, jwt_claims: JwtClaims, headers: dict) -> dict:
        headers['Authorization'] = 'Bearer {}'.format(encode_jwt(jwt_claims))
        return headers
