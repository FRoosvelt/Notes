from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db_api.commands.notes import select_all_notes
from keyboards.start import keyboard_start


# Функция просмотора заметок
async def read_notes(message: Message):
    keyboard = keyboard_start()
    if not await select_all_notes(message.from_user.id):
        return await message.answer(" ❌У вас пока нет заметок", reply_markup=keyboard)
    else:
        notes = await select_all_notes(message.from_user.id)
        for note in notes:
            await message.answer(f" <b>Номер заметки: {note.id}</>\n"
                                 f" <b>Заголовок: {note.title}</>\n"
                                 f" <i>Содержание: {note.description}</>", reply_markup=keyboard)


# Регистер просмотра заметок
def register_read_notes(dp: Dispatcher):
    dp.register_message_handler(
        read_notes,
        Text("👓Посмотреть заметки")
    )
