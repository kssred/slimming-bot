from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from src.config import TGBOT_TOKEN


dp = Dispatcher()
bot = Bot(token=TGBOT_TOKEN, parse_mode=ParseMode.HTML)  # type: ignore


__all__ = ["bot", "dp"]
