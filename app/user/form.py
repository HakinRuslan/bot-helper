from aiogram.fsm.state import StatesGroup, State

class Revinfo(StatesGroup):
    type_of_problem = State()
    coffee = State()
    desc = State()

class RevRealinfo(StatesGroup):
    type_of_problem = State()
    coffee = State()
    desc = State()