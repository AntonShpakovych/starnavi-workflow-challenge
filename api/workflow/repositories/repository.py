from abc import ABC, abstractmethod
from typing import TypeVar

from api.dependencies import AsyncSession
from api.models import Base


T = TypeVar("T", bound=Base)


class Repository(ABC):
    """
    An abstract repository for all model repositories that implement simple CRUD
    """
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    @abstractmethod
    async def create(self, *args, **kwargs) -> T:
        pass

    @abstractmethod
    async def get_one(self, *args, **kwargs) -> T:
        pass

    @abstractmethod
    async def get_all(self) -> list[T]:
        pass

    @abstractmethod
    async def update(self, *args, **kwargs) -> T:
        pass

    @abstractmethod
    async def delete(self, *args, **kwargs) -> T:
        pass
