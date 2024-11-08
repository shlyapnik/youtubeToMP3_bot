from aiogram.fsm.state import State, StatesGroup

class Download(StatesGroup):
    waiting_for_url = State() 