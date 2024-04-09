from aiogram.types import Message
from src.loader import dp


@dp.message()
async def error_handler(message: Message) -> None:
    await message.answer("К сожалению я не знаю как ответить на ваш запрос")
