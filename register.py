from aiogram import Dispatcher

from handlers.add_note import register_add_note
from handlers.delete_note import register_delete_note
from handlers.read_notes import register_read_notes
from handlers.search_note import register_search_notes
from handlers.start import register_start


# Главный регистер
def register(dp: Dispatcher):
    register_start(dp)
    register_add_note(dp)
    register_read_notes(dp)
    register_search_notes(dp)
    register_delete_note(dp)
