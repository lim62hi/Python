from aiogram import types, Dispatcher
from create import dp, bot
from keyboards.client_kb import kb_user
from other import HELP

async def help_start(message : types.message):
    bot.reply(HELP)

def reg(dp : Dispatcher):
    dp.register_message_handler(help_start, 'start')