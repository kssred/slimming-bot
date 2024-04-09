from typing import Optional, Union

from aiogram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


class MessageService:
    def __init__(self) -> None:
        self.sender = ...

    async def send_message(
        self,
        chat_id: int,
        text: str,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ):
        pass
