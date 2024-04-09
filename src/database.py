from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import BASE_DIR

async_engine = create_async_engine(f"sqlite+aiosqlite:///{BASE_DIR / 'db.db'}")


class BaseModel(DeclarativeBase):
    pass
