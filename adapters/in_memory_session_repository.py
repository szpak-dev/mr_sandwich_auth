from pickle import loads, dumps

from domain.errors import SessionNotFound
from domain.ports.session_repository import SessionRepository
from domain.value_objects import Session, SessionId, UserId
from shared.shared import generate_number_base64

sessions_by_id = {}
sessions_by_user_id = {}


class InMemorySessionRepository(SessionRepository):
    def create_session(self, user_id: UserId) -> Session:
        session = Session(
            SessionId(generate_number_base64(40)),
            user_id,
        )

        serialized_session = dumps(session)
        sessions_by_id[session.id.value] = serialized_session
        sessions_by_user_id[user_id.id] = serialized_session
        return session

    def get_by_id(self, session_id: SessionId) -> Session:
        session = sessions_by_id.get(session_id.value)
        if not session:
            raise SessionNotFound

        return loads(session)

    def destroy_session(self, session_id: SessionId) -> None:
        session = self.get_by_id(session_id)

        raw_session_id = session.id.value
        sessions_by_id.pop(raw_session_id)

        raw_user_id = session.user_id.id
        sessions_by_user_id.pop(raw_user_id)
