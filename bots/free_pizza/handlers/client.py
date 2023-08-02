from aiogram import types, Dispatcher
from create import bot
from keyboards.client_kb import kb_client, kb_inline
from keyboards.admin_kb import kb_admin
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import read_info

HELP = 'Вы можете узнать расписание работы, расположение и меню\nПриятного аппетита!'
rej = 'Пн - пт 8:00 - 20:00, сб 10:00 - 18:00'
rasp = 'Улица Колбасная, 15А'


async def Help(message : types.message):
    if message.from_user.id == 5221868883:
        await message.delete()
        await bot.send_message(message.from_user.id, 'Добро пожаловать в бота нашей пиццерии Free Pizza!', reply_markup=kb_admin)
        await bot.send_message(message.from_user.id, HELP + '\n\nВы вошли как Администратор', reply_markup=kb_inline) 
    else:
        await message.delete()
        await bot.send_message(message.from_user.id, 'Добро пожаловать в бота нашей пиццерии Free Pizza!', reply_markup=kb_client)
        await bot.send_message(message.from_user.id, HELP, reply_markup=kb_inline)

async def rejim(message : types.message):
    await bot.send_message(message.from_user.id, rej)

async def ras(message : types.message):
    await bot.send_message(message.from_user.id, rasp)

async def menu(message : types.message):
    await read_info(message.from_user.id)

async def call_menu(callback : types.CallbackQuery):
    await callback.message.answer('Меню Free Pizza:')
    await read_info(callback.from_user.id)
    await callback.answer()

def reg(dp : Dispatcher):
    dp.register_message_handler(Help, commands=['start'])
    dp.register_message_handler(rejim, commands=['режим'])
    dp.register_message_handler(rejim, Text(equals=['режим'], ignore_case=True))
    dp.register_message_handler(ras, commands=['место'])
    dp.register_message_handler(ras, Text(equals=['место'], ignore_case=True))
    dp.register_message_handler(menu, commands=['меню'])
    dp.register_message_handler(menu, Text(equals=['меню'], ignore_case=True))
    dp.register_callback_query_handler(call_menu, text='меню')