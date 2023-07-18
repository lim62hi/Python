from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

b1 = KeyboardButton('/загрузить')
b2 = KeyboardButton('/место')
b3 = KeyboardButton('/режим')
b4 = KeyboardButton('/меню')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(b1).row(b2, b3).add(b4)

b2 = KeyboardButton('/отмена')
kb_onload = ReplyKeyboardMarkup(resize_keyboard=True)
kb_onload.add(b2)