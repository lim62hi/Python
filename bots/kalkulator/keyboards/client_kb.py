from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('пример')
b2 = KeyboardButton('сложить')
b3 = KeyboardButton('вычесть')
b4 = KeyboardButton('умножить')
b5 = KeyboardButton('разделить')
kb_user = ReplyKeyboardMarkup(resize_keyboard=True)
kb_user.add(b1).row(b2, b3).row(b4, b5)

b6 = KeyboardButton('отмена')
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(b6)