import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_NAME = os.getenv("POSTGRES_NAME")


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"
)


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = SQLALCHEMY_DATABASE_URL
