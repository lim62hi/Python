from aiogram import types, Dispatcher

HELP = '''Команда не найдена!

Выбери на клавиатуре то, что ты хочешь сделать'''

async def Help(message : types.message):
    await message.reply(HELP)

def reg(dp : Dispatcher):
    dp.register_message_handler(Help)