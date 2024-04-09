from aiogram.fsm.state import StatesGroup, State


class RegisterStates(StatesGroup):
    weight = State()
    activity = State()
