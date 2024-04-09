from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseModel
from src.models.types import created_at, int_pk


class PhysicalModel(BaseModel):
    __tablename__ = "user_physical"

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    kcal: Mapped[float]
    created_at: Mapped[created_at]
