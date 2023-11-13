from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки при команде start
def keyboard_start():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton("✏️Добавить новую заметку"),
                                           KeyboardButton("👓Посмотреть заметки")
                                       ],
                                       [
                                           KeyboardButton("🔎Поиск заметки")
                                       ],
                                       [
                                           KeyboardButton("❌Удалить заметку")
                                       ]
                                   ]
                                   )
    return keyboard
