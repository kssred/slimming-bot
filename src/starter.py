from aiogram.types import BotCommand

from src.models import BaseModel
from src.database import async_engine
from src.handlers import dp
from src.loader import bot


async def run_polling():
    await _set_commands()
    await _create_tables()

    print("Бот успешно запущен")

    await dp.start_polling(bot)


async def _create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)


async def _set_commands():
    await bot.set_my_commands(
        commands=[
            BotCommand(command="start", description="Запуск бота"),
            BotCommand(command="activity", description="Изменить уровень активности"),
        ]
    )

    print("Команды бота установлены")
