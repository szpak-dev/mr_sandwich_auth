from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class JwtClaims:
    sub: str
    roles: List[str]
