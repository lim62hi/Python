from aiogram import types, Dispatcher
from create import bot
from keyboards.client_kb import *
from keyboards.admin_kb import *
from aiogram.dispatcher.filters import Text
from data_base.sqlite_db import read_info
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

HELP = 'Вы можете узнать расписание работы, расположение и меню\nПриятного аппетита!'
rej = 'Пн - пт 8:00 - 20:00, сб 10:00 - 18:00'
rasp = 'Улица Колбасная, 15А'

dat = None
pizza = None

class FSM_client(StatesGroup):
    number = State()
    name = State()

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

async def zak(callback : types.CallbackQuery):
    await FSM_client.number.set()
    global dat, pizza
    dat = []
    pizza = ''
    call = callback.data.split()
    call.pop(0)
    for i in call:
        pizza += i
    await bot.send_message(callback.from_user.id, 'Введите ваш номер телефона, который мы можем использовать для связи', reply_markup=kb_onload)
    await callback.answer()

async def cancel(message : types.message, state : FSMContext):
    await state.finish()
    if message.from_user.id == 5221868883:
        await bot.send_message(message.from_user.id, 'Загрузка отменена!', reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, 'Загрузка отменена!', reply_markup=kb_client)

async def num_zak(message : types.message, state : FSMContext):
    try:
        global dat
        dat.append(int(message.text))
        await message.reply('Как вас зовут?')
        await FSM_client.next()
    except:
        await message.reply('Введите корректный номер')
        FSMContext.reset()

async def name_zak(message : types.message, state : FSMContext):
    global dat, pizza
    dat.append(message.text)
    await bot.send_message(5221868883, f'@{message.from_user.username} заказал {pizza.lower()}\nТелефон: {dat[0]}\nИмя: {dat[1].capitalize()}')
    await state.finish()
    if message.from_user.id == 5221868883:
        await bot.send_message(message.from_user.id, f'{dat[1]}, вы успешно заказали пиццу!', reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, f'{dat[1]}, Вы успешно заказали пиццу!', reply_markup=kb_client)

def reg(dp : Dispatcher):
    dp.register_message_handler(Help, commands=['start'])
    dp.register_message_handler(rejim, commands=['режим'])
    dp.register_message_handler(rejim, Text(equals=['режим'], ignore_case=True))
    dp.register_message_handler(ras, commands=['место'])
    dp.register_message_handler(ras, Text(equals=['место'], ignore_case=True))
    dp.register_message_handler(menu, commands=['меню'])
    dp.register_message_handler(menu, Text(equals=['меню'], ignore_case=True))
    dp.register_callback_query_handler(call_menu, text='меню')
    dp.register_callback_query_handler(zak, lambda x: x.data and x.data.startswith('заказать '))
    dp.register_message_handler(cancel, commands=['отмена'], state='*')
    dp.register_message_handler(cancel, Text(equals=['отмена'], ignore_case=True), state='*')
    dp.register_message_handler(num_zak, state=FSM_client.number)
    dp.register_message_handler(name_zak, state=FSM_client.name)