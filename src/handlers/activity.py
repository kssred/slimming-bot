from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.enums import ActivityEnum
from src.filters.private import IsPrivateFilter
from src.keyboards.kbm import activity_index_kbm, base_kbm
from src.loader import dp
from src.services.db import database
from src.services.exceptions import InvalidValue
from src.services.inputs import input_service
from src.states.input import InputStates
from src.texts import GET_ACTIVITY, UPDATE_ACTIVITY


@dp.message(IsPrivateFilter(), F.text == "/activity")
async def start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(InputStates.get_activity)

    await message.answer(GET_ACTIVITY.capitalize(), reply_markup=activity_index_kbm)


@dp.message(InputStates.get_activity)
async def start_get_activity(message: Message, state: FSMContext) -> None:
    try:
        activity = await input_service.get_activity(message.text)
    except InvalidValue:
        await message.answer(
            f"Пожалуйста введите верное число от {ActivityEnum.ONE} до {ActivityEnum.FIVE}"
        )
        return

    await database.update_user(message.from_user.id, activity=activity)

    await state.clear()
    await message.answer(UPDATE_ACTIVITY, reply_markup=base_kbm)
