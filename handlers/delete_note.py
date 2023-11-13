from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from db_api.commands.notes import select_all_notes, delete_note, select_id_notes
from keyboards.start import keyboard_start
from states.delete_notes import Delete_note


# Функция на текст ❌Удалить заметку
async def delete_notes_keyboard(message: Message):
    if not await select_all_notes(message.from_user.id):
        return await message.answer(" ❌У вас пока нет заметок")
    else:
        await Delete_note.id.set()
        return await message.answer(" 👇Введите номер заметки для удаления")


# Функция на удаление заметки в боте
async def delete_notes(message: Message, state: FSMContext):
    keyboard = keyboard_start()
    id = message.text
    if not await select_id_notes(user_id=message.from_user.id, id=id):
        await state.finish()
        return await message.answer(" ❌У вас нет такого номера заметки", reply_markup=keyboard)
    else:
        await state.finish()
        await delete_note(id=id)
        return await message.answer(" ❌Ваша заметка была удалена", reply_markup=keyboard)


def register_delete_note(dp: Dispatcher):
    dp.register_message_handler(
        delete_notes_keyboard,
        Text("❌Удалить заметку")
    )
    dp.register_message_handler(
        delete_notes,
        state=Delete_note.id
    )
