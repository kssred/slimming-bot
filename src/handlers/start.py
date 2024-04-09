from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.enums import ActivityEnum
from src.filters.private import IsPrivateFilter
from src.keyboards.kbm import activity_index_kbm, base_kbm
from src.loader import dp
from src.services.db import database
from src.services.exceptions import InvalidValue
from src.services.inputs import input_service
from src.states.register import RegisterStates
from src.texts import GET_ACTIVITY, GET_WEIGHT, REGISTER_END, START


@dp.message(IsPrivateFilter(), CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    await database.add_user(message.from_user)

    if message.from_user.first_name:
        username = message.from_user.first_name
    else:
        username = message.from_user.username

    if username:
        message_text = f"Здравствуйте, {username}! {START}"
    else:
        message_text = f"Здравствуйте! {START}"

    await message.answer(message_text, reply_markup=base_kbm)

    await state.set_state(RegisterStates.weight)
    await message.answer(GET_WEIGHT)


@dp.message(RegisterStates.weight)
async def start_get_weight(message: Message, state: FSMContext) -> None:
    try:
        weight = await input_service.get_weight(message.text)
    except InvalidValue:
        await message.answer('Пожалуйста введите вес в верном формате. Например "78.5"')
        return

    await database.add_weight(message.from_user.id, weight)

    await state.set_state(RegisterStates.activity)
    await message.answer(f"А теперь, {GET_ACTIVITY}", reply_markup=activity_index_kbm)


@dp.message(RegisterStates.activity)
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
    await message.answer(REGISTER_END, reply_markup=base_kbm)
