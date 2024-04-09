from enum import StrEnum

from aiogram.filters.callback_data import CallbackData


class ReportType(StrEnum):
    TEN = "10"
    MONTH = "30"
    OTHER = "other"


class ReportCallbackData(CallbackData, prefix="report"):
    kind: ReportType
