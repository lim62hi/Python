from aiogram import types, Dispatcher
from create import dp

HELP = '''Привет!
В этом боте ты с легкостью можешь выполнять простые математические действия: сложение, вычитание, умножение и деление

Чтобы попробовать бота воспользуйся клавиатурой!'''

async def Help(message : types.message):
    await message.reply(HELP)

def reg(dp : Dispatcher):
    dp.register_message_handler(Help)