from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import async_session


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session


Session = Annotated[AsyncSession, Depends(get_async_session)]
