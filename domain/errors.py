from shared.shared import docstring_message
from shared.ddd import DomainError


@docstring_message
class SessionError(DomainError):
    """Session error"""


@docstring_message
class IdentityNotFound(SessionError):
    """Identity was not found within Request"""


@docstring_message
class SessionNotFound(SessionError):
    """Session not found"""


@docstring_message
class JwtClaimsNotFound(SessionError):
    """JWT claims not found"""


@docstring_message
class UserError(DomainError):
    """User error"""


@docstring_message
class UserAlreadyExists(UserError):
    """User already exists"""


@docstring_message
class UserNotFound(UserError):
    """User not found"""


@docstring_message
class PasswordDoesNotMatch(UserError):
    """Password is invalid"""
