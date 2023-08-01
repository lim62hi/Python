from aiogram import types, Dispatcher
from create import bot
from keyboards.client_kb import kb_client
from keyboards.admin_kb import kb_admin
from data_base.sqlite_db import read_info

HELP = 'Приятного аппетита!'
rej = 'Режим работы: любой день недели 8:00 - 20:00'
rasp = 'Улица Колбасная, 15А'
ls = 'Пожалуйста, напишите мне в личные сообщения, чтобы я мог с Вами общаться через них и присылать Вам личную информацию!'


async def Help(message : types.message):
    try:
        await bot.send_message(message.from_user.id, HELP, reply_markup=kb_client)
        await message.delete()
        if 5221868883 == message.from_user.id:
            await bot.send_message(message.from_user.id, 'Вы вошли как Администратор', reply_markup=kb_admin)
    except:
        await message.reply(f'{HELP}\n\n{ls}')

async def rejim(message : types.message):
    try:
        await bot.send_message(message.from_user.id, rej)
    except:
        await message.reply(f'{rej}\n\n{ls}')

async def ras(message : types.message):
    try:
        await bot.send_message(message.from_user.id, rasp)
    except:
        await message.reply(f'{rasp}\n\n{ls}')

async def menu(message : types.message):
    await read_info(message)

def reg(dp : Dispatcher):
    dp.register_message_handler(Help, commands=['start'])
    dp.register_message_handler(rejim, commands=['режим'])
    dp.register_message_handler(ras, commands=['место'])
    dp.register_message_handler(menu, commands=['меню'])