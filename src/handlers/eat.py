from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.filters.private import IsPrivateFilter
from src.loader import dp
from src.services.db import database
from src.services.exceptions import InvalidValue
from src.services.inputs import input_service
from src.states import InputStates
from src.texts import ADD_EAT, GET_EAT


@dp.message(IsPrivateFilter(), F.text == "Еда")
async def eat_handler(message: Message, state: FSMContext) -> None:
    await message.answer(GET_EAT)

    await state.set_state(InputStates.get_eat)


@dp.message(InputStates.get_eat)
async def get_eat(message: Message, state: FSMContext) -> None:
    try:
        eat_kcal = await input_service.get_positive_int(message.text)
    except InvalidValue:
        await message.answer('Пожалуйста введите kcal в верном формате. Например "432"')
        return

    await database.add_eat(message.from_user.id, kcal=eat_kcal)

    await state.clear()
    # TODO выводить отчёт за текущий день
    await message.answer(ADD_EAT)
