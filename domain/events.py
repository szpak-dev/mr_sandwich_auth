from json import dumps
from shared.ddd import DomainEvent


class AuthenticationFailedEvent(DomainEvent):
    def __init__(self, user_id: str):
        super().__init__('auth.user.authentication_failed')
        self._user_id = user_id

    def serialize(self) -> str:
        return dumps({'user_id': self._user_id})


class AuthenticationSuccess(DomainEvent):
    def __init__(self, user_id: str):
        super().__init__('auth.user.authentication_success')
        self._user_id = user_id

    def serialize(self) -> str:
        return dumps({'user_id': self._user_id})
