from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('Загрузить')
b2 = KeyboardButton('Меню')
b3 = KeyboardButton('Режим')
b4 = KeyboardButton('Место')
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.row(b1, b2).row(b3, b4)

b1 = KeyboardButton('Отмена')
kb_onload = ReplyKeyboardMarkup(resize_keyboard=True)
kb_onload.add(b1)