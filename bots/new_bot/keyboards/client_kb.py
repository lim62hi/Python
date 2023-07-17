from aiogram.types import KeyboardButton, ReplyKeyboardRemove, ReplyKeyboardMarkup

b1 = KeyboardButton('/меню')
b2 = KeyboardButton('/режим')
b3 = KeyboardButton('/место')
b4 = KeyboardButton('Номер', request_contact=True)

num = ReplyKeyboardMarkup(resize_keyboard=True)
num.add(b4)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).row(b2, b3)