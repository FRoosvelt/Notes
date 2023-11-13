from aiogram.dispatcher.filters.state import StatesGroup, State


# Состояние для удаление заметок
class Delete_note(StatesGroup):
    id = State()
