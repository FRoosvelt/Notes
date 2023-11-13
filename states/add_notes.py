from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояние для добавление заметок
class Add_notes(StatesGroup):
    title = State()
    description = State()
