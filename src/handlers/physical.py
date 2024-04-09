from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.filters.private import IsPrivateFilter
from src.loader import dp
from src.services.db import database
from src.services.exceptions import InvalidValue
from src.services.inputs import input_service
from src.states import InputStates
from src.texts import ADD_PHYSICAL, GET_PHYSICAL


@dp.message(IsPrivateFilter(), F.text == "Физ. активность")
async def physical_handler(message: Message, state: FSMContext) -> None:
    await message.answer(GET_PHYSICAL)

    await state.set_state(InputStates.get_physical)


@dp.message(InputStates.get_physical)
async def get_physical(message: Message, state: FSMContext) -> None:
    try:
        physical_kcal = await input_service.get_positive_int(message.text)
    except InvalidValue:
        await message.answer('Пожалуйста введите kcal в верном формате. Например "432"')
        return

    await database.add_physical(message.from_user.id, kcal=physical_kcal)

    await state.clear()
    # TODO выводить отчёт за текущий день
    await message.answer(ADD_PHYSICAL)
