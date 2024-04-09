from typing import Optional

from src.enums import ActivityEnum
from src.services.exceptions import InvalidValue
from src.validators.numeric import is_float, is_integer


class InputService:
    async def get_weight(self, text: Optional[str]) -> float:
        if not text:
            raise InvalidValue

        text = text.replace(",", ".")
        if not is_float(text):
            raise InvalidValue

        weight = float(text)
        if weight <= 0:
            raise InvalidValue

        return weight

    async def get_activity(self, text: Optional[str]) -> int:
        if text not in ActivityEnum:
            raise InvalidValue

        return await self.get_positive_int(text)

    async def get_positive_int(self, text: Optional[str]) -> int:
        if not text:
            raise InvalidValue

        if not is_integer(text):
            raise InvalidValue

        int_value = int(text)

        if int_value < 0:
            raise InvalidValue

        return int_value


input_service = InputService()
