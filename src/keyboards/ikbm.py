from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.callbacks.report import ReportCallbackData, ReportType


report_ikbm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="За 10 дней",
                callback_data=ReportCallbackData(kind=ReportType.TEN).pack(),
            ),
            InlineKeyboardButton(
                text="За месяц",
                callback_data=ReportCallbackData(kind=ReportType.MONTH).pack(),
            ),
        ],
        [
            InlineKeyboardButton(
                text="Больше",
                callback_data=ReportCallbackData(kind=ReportType.OTHER).pack(),
            )
        ],
    ],
    row_width=2,
)
