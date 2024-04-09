from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.filters.private import IsPrivateFilter
from src.loader import dp
from src.services.db import database
from src.services.exceptions import InvalidValue
from src.services.inputs import input_service
from src.states import InputStates
from src.texts import ADD_WEIGHT, GET_WEIGHT


@dp.message(IsPrivateFilter(), F.text == "Вес")
async def weight_handler(message: Message, state: FSMContext) -> None:
    await message.answer(GET_WEIGHT)

    await state.set_state(InputStates.get_weight)


@dp.message(InputStates.get_weight)
async def get_weight(message: Message, state: FSMContext) -> None:
    try:
        weight = await input_service.get_weight(message.text)
    except InvalidValue:
        await message.answer('Пожалуйста введите вес в верном формате. Например "78.5"')
        return

    await database.add_weight(message.from_user.id, weight=weight)

    await state.clear()
    await message.answer(ADD_WEIGHT)
