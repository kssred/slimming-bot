from aiogram import F
from aiogram.types import CallbackQuery, Message

from src.callbacks.report import ReportCallbackData, ReportType
from src.filters.private import IsPrivateFilter
from src.keyboards.ikbm import report_ikbm
from src.loader import dp


@dp.message(IsPrivateFilter(), F.text == "Отчёт")
async def report_handler(message: Message) -> None:
    await message.answer(
        "Пожалуйста выберите необходимый вид отчёта", reply_markup=report_ikbm
    )


@dp.callback_query(
    IsPrivateFilter(), ReportCallbackData.filter(F.kind == ReportType.TEN)
)
async def report_ten_days(callback: CallbackQuery):
    await callback.message.answer("123")


@dp.callback_query(
    IsPrivateFilter(), ReportCallbackData.filter(F.kind == ReportType.MONTH)
)
async def report_month(callback: CallbackQuery):
    pass


@dp.callback_query(
    IsPrivateFilter(), ReportCallbackData.filter(F.kind == ReportType.OTHER)
)
async def report_other(callback: CallbackQuery):
    pass
