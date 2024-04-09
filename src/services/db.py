from typing import Union
from aiogram.types import User
from sqlalchemy import Insert, Update, insert, select, update
from sqlalchemy.exc import DBAPIError
from sqlalchemy.exc import IntegrityError, MultipleResultsFound, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.database import async_engine
from src.models.eat import EatModel
from src.models.physical import PhysicalModel
from src.models.user import UserModel
from src.models.weight import WeightModel


class DatabaseORM:
    def __init__(self) -> None:
        self.session = async_sessionmaker(async_engine, class_=AsyncSession)

    async def get_user(self, id_: int) -> UserModel:
        query = select(UserModel).filter_by(id=id_)
        async with self.session() as s:
            result = await s.execute(query)

        try:
            return result.scalar_one()
        except (NoResultFound, MultipleResultsFound):
            raise

    async def add_user(self, user: User) -> bool:
        stmt = insert(UserModel).values(
            id=user.id,
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
        )
        return await self._execute_stmt(stmt)

    async def update_user(self, user_id: int, **data) -> bool:
        stmt = update(UserModel).filter_by(id=user_id).values(**data)
        return await self._execute_stmt(stmt)

    async def add_weight(self, user_id: int, weight: float) -> bool:
        stmt = insert(WeightModel).values(user_id=user_id, kilos=weight)
        return await self._execute_stmt(stmt)

    async def add_eat(self, user_id: int, kcal: float) -> bool:
        stmt = insert(EatModel).values(user_id=user_id, kcal=kcal)
        return await self._execute_stmt(stmt)

    async def add_physical(self, user_id: int, kcal: float) -> bool:
        stmt = insert(PhysicalModel).values(user_id=user_id, kcal=kcal)
        return await self._execute_stmt(stmt)

    async def get_report_info(self, user_id: int, days: int):
        pass

    async def _execute_stmt(self, stmt: Union[Insert, Update]) -> bool:
        async with self.session() as s:
            try:
                await s.execute(stmt)
            except DBAPIError:
                return False

            await s.commit()

        return True


database = DatabaseORM()
