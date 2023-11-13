import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from aiogram.utils import executor

from data.config import BOT_TOKEN
from db_api.database import create_base
from register import register


# Функция на запуск проекта
async def on_startup(dp: Dispatcher):
    register(dp)
    await create_base()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    storage = MemoryStorage()
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot, storage=storage)
    executor.start_polling(dp, on_startup=on_startup)
