from aiogram import types, Dispatcher

async def ban_word(message : types.message):
    await message.reply('Команда не найдена!')

def reg(dp : Dispatcher):
    dp.register_message_handler(ban_word)