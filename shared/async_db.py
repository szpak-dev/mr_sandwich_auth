from __future__ import annotations

from os import getenv

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base


class Database:
    def __init__(self, dsn: str):
        self._engine = create_async_engine(
            dsn,
            echo=True,
        )

        self._session: AsyncSession = AsyncSession(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    def current_session(self) -> AsyncSession:
        return self._session


database = Database(getenv(
    'DATABASE_DSN',
    'postgresql+asyncpg://postgres:postgres@localhost:5433/auth',
))

Base = declarative_base()
