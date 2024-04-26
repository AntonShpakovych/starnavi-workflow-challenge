from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession as AsyncSessionSQLAlchemy

from api.database import async_session


async def get_async_session() -> AsyncSessionSQLAlchemy:
    async with async_session() as session:
        yield session


AsyncSession = Annotated[AsyncSessionSQLAlchemy, Depends(get_async_session)]
