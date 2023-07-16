from aiogram import types, Dispatcher
from string import punctuation
from json import load
from create import dp

async def ban_word(message : types.message):
    if {i.lower().translate(str.maketrans('', '', punctuation)) for i in message.text.split()}\
    .intersection(set(load(open('words.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()

def reg(dp : Dispatcher):
    dp.register_message_handler(ban_word)