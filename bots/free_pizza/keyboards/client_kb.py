from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('Меню')
b2 = KeyboardButton('Режим')
b3 = KeyboardButton('Место')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).row(b2, b3)

kb_inline = InlineKeyboardMarkup()
b1 = InlineKeyboardButton(text='Показать меню', callback_data='меню')
kb_inline.add(b1)