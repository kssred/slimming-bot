from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseModel
from src.models.types import int_pk, created_at, updated_at


class UserModel(BaseModel):
    __tablename__ = "user"

    id: Mapped[int_pk]
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(String(32))
    first_name: Mapped[Optional[str]] = mapped_column(String(255))
    last_name: Mapped[Optional[str]] = mapped_column(String(255))
    activity: Mapped[Optional[int]]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
