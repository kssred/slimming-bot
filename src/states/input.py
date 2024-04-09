from aiogram.fsm.state import StatesGroup, State


class InputStates(StatesGroup):
    get_weight = State()
    get_eat = State()
    get_physical = State()
    get_activity = State()
