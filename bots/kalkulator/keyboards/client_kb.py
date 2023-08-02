from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('Пример')
b2 = KeyboardButton('Сложить')
b3 = KeyboardButton('Вычесть')
b4 = KeyboardButton('Умножить')
b5 = KeyboardButton('Разделить')
kb_user = ReplyKeyboardMarkup(resize_keyboard=True)
kb_user.add(b1).row(b2, b3).row(b4, b5)

b1 = KeyboardButton('Отмена')
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(b1)

kb_inline = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Помощь', callback_data='помощь')
kb_inline.add(b1)