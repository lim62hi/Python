from aiogram import types, Dispatcher
from create import dp, bot

HELP = '''/help - список команд
/work - режим работы
/location - расположение кафе

Приятного аппетита!'''
rej = 'Режим работы: любой день недели 8:00 - 20:00'
rasp = 'Улица Колбасная, 15А'
ls = 'Пожалуйста, напишите мне в личные сообщения, чтобы я мог с Вами общаться через них и присылать Вам личную информацию!'


async def Help(message : types.message):
    try:
        await bot.send_message(message.from_user.id, HELP)
        await message.delete()
    except:
        await message.reply(f'{HELP}\n\n{ls}')

async def rejim(message : types.message):
    try:
        await bot.send_message(message.from_user.id, rej)
        await message.delete()
    except:
        await message.reply(f'{rej}\n\n{ls}')

async def ras(message : types.message):
    try:
        await bot.send_message(message.from_user.id, rasp)
        await message.delete()
    except:
        await message.reply(f'{rasp}\n\n{ls}')

def reg(dp : Dispatcher):
    dp.register_message_handler(Help, commands=['start', 'help'])
    dp.register_message_handler(rejim, commands=['work'])
    dp.register_message_handler(ras, commands=['location'])