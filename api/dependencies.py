from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.config import Settings
from api.database import async_session


@lru_cache
def get_settings() -> Settings:
    return Settings()


Settings = Annotated[Settings, Depends(get_settings)]


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session


Session = Annotated[AsyncSession, Depends(get_async_session)]
