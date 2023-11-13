from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db_api.commands.notes import add_new_note
from db_api.tables.notes import Notes_table
from keyboards.start import keyboard_start
from states.add_notes import Add_notes


# Функция на текст ✏️Добавить новую заметку
async def add_note(message: Message):
    await Add_notes.title.set()
    return await message.answer(" 👇Введите заголовок заметки")


# Функция на сохранение названия заметки
async def note_title(message: Message, state: FSMContext):
    await Add_notes.description.set()
    title = message.text
    note = Notes_table()
    note.title = title
    await state.update_data(note=note)
    return await message.answer(" 👇Введите содержание заметки")


# Функция на добавление заметки в боте
async def note_text(message: Message, state: FSMContext):
    data = await state.get_data()
    note = data.get("note")
    title = note.title
    description = message.text
    await add_new_note(user_id=message.from_user.id, title=title, description=description)
    await state.finish()
    keyboard = keyboard_start()
    return await message.answer(" ✅Ваша заметка успешна добавлена", reply_markup=keyboard)


# Регистер на добавление заметки
def register_add_note(dp: Dispatcher):
    dp.register_message_handler(
        add_note,
        Text("✏️Добавить новую заметку")
    )
    dp.register_message_handler(
        note_title,
        state=Add_notes.title
    )
    dp.register_message_handler(
        note_text,
        state=Add_notes.description
    )
