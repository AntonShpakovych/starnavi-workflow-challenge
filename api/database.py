from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker


from .dependencies import get_settings


SQLALCHEMY_DATABASE_URL = get_settings().SQLALCHEMY_DATABASE_URL

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)
