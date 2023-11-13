from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

from keyboards.start import keyboard_start


# Функция команды start
async def start(message: Message):
    keyboard = keyboard_start()
    return await message.answer("Выберите любую команду", reply_markup=keyboard)


# Регистер на команду start
def register_start(dp: Dispatcher):
    dp.register_message_handler(
        start,
        CommandStart()
    )
