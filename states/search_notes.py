from aiogram.dispatcher.filters.state import StatesGroup, State


# Соcтояние для поиска заметок
class Search_notes(StatesGroup):
    keyword = State()
