from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from src.enums import ActivityEnum

base_kbm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Вес")],
        [KeyboardButton(text="Еда"), KeyboardButton(text="Физ. активность")],
        [KeyboardButton(text="Отчёт")],
    ],
    resize_keyboard=True,
)


activity_index_kbm = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=e.value) for e in ActivityEnum]],
    resize_keyboard=True,
)
