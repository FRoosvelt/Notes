from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db_api.commands.notes import \
    select_description_search_notes, select_all_notes
from keyboards.start import keyboard_start
from states.search_notes import Search_notes


# Функция на текст 🔎Поиск заметки
async def search_note(message: Message):
    if not await select_all_notes(message.from_user.id):
        return await message.answer(" ❌У вас пока нет заметок")
    else:
        await Search_notes.keyword.set()
        return await message.answer(" 👇Введите фразу или ключевое слова из описания заметки")


# Функция поска по фразе
async def search_note_keyword(message: Message, state: FSMContext):
    await state.finish()
    keyboard = keyboard_start()
    keyword = message.text
    if not await select_description_search_notes(user_id=message.from_user.id, keyword=keyword):
        return await message.answer(" ❌По вашему запросу ничего не найдено", reply_markup=keyboard)
    else:
        for note in await select_description_search_notes(user_id=message.from_user.id, keyword=keyword):
            await message.answer(f" <b>Номер заметки: {note.id}</>\n"
                                 f" <b>Заголовок: {note.title}</>\n"
                                 f" <i>Содержание: {note.description}</>", reply_markup=keyboard)


# Регистер поиска заметок
def register_search_notes(dp: Dispatcher):
    dp.register_message_handler(
        search_note,
        Text("🔎Поиск заметки")
    )
    dp.register_message_handler(
        search_note_keyword,
        state=Search_notes.keyword
    )
