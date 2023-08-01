from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

b1 = KeyboardButton('/загрузить')
b2 = KeyboardButton('/удалить')
b3 = KeyboardButton('/меню')
b4 = KeyboardButton('/режим')
b5 = KeyboardButton('/место')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.row(b1, b2).add(b3).row(b4, b5)

b1 = KeyboardButton('/отмена')
kb_onload = ReplyKeyboardMarkup(resize_keyboard=True)
kb_onload.add(b1)