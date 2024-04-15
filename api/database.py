from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from .dependencies import get_settings


SQLALCHEMY_DATABASE_URL = get_settings().SQLALCHEMY_DATABASE_URL

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_`%(constraint_name)s`",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })
