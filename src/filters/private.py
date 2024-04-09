from typing import Union
from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message


class IsPrivateFilter(Filter):
    async def __call__(self, obj: Union[Message, CallbackQuery]) -> bool:
        return obj.chat.id == obj.from_user.id
