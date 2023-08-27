import sqlite3 as sq
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

storage = MemoryStorage()
bot = Bot(token='5967826376:AAFE57ErW9QHAEPzaNo-vncjSJrZVtyC7W8')
dp = Dispatcher(bot, storage=storage)
HELP = 'Вы можете узнать расписание работы, расположение и меню\nПриятного аппетита!'
rej = 'Пн - пт 8:00 - 20:00, сб 10:00 - 18:00'
rasp = 'Улица Колбасная, 15А'
dat = None
pizza = None
base = None
cur = None
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton('Загрузить'), KeyboardButton('Меню')).row(KeyboardButton('Режим'), KeyboardButton('Место'))
kb_onload = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))
kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Меню')).row(KeyboardButton('Режим'), KeyboardButton('Место'))
kb_inline = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Показать меню', callback_data='меню'))

class FSM_client(StatesGroup):
    number = State()
    name = State()
class FSM_admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def start_bot(_):
    sq_start()
    print('Бот включился и исправно работает!')

def sq_start():
    global base, cur 
    base = sq.connect('bots\\free_pizza\pizza.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT, description TEXT, price TEXT)')
    base.commit()

async def load_info(state):
    global cur, base
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        base.commit()

async def read_info(id):
    global cur
    if id == 5221868883:
        for el in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_photo(id, el[0], f'{el[1]}\nОписание: {el[2]}\nЦена: {el[3]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {el[1]}', callback_data=f'удалить {el[1]}')).add(InlineKeyboardButton('Заказать', callback_data=f'заказать {el[1]}')))
    else:
        for el in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_photo(id, el[0], f'{el[1]}\nОписание: {el[2]}\nЦена: {el[3]}', reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton('Заказать', callback_data=f'заказать {el[1]}')))

async def del_info(name):
    global cur, base
    cur.execute('DELETE FROM menu WHERE name == ?', (name,))
    base.commit()

@dp.message_handler(commands=['загрузить'], state=None)
@dp.message_handler(Text(equals=['загрузить'], ignore_case=True), state=None)
async def load(message : types.message):
    if message.from_user.id == 5221868883:
        await FSM_admin.photo.set()
        await bot.send_message(message.from_user.id, 'Начинаю загрузку', reply_markup=kb_onload)
        await message.reply('Загрузите фото')

@dp.message_handler(commands=['отмена'], state='*')
@dp.message_handler(Text(equals=['отмена'], ignore_case=True), state='*')
async def cancel(message : types.message, state : FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, 'Загрузка отменена!', reply_markup=kb_admin)

@dp.message_handler(content_types=['photo'], state=FSM_admin.photo)
async def load_photo(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_admin.next()
    await message.reply('Введите название')

@dp.message_handler(state=FSM_admin.name)
async def load_name(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_admin.next()
    await message.reply('Введите описание')

@dp.message_handler(state=FSM_admin.description)
async def load_description(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_admin.next()
    await message.reply('Введите цену')

@dp.message_handler(state=FSM_admin.price)
async def load_price(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
    await load_info(state)
    await bot.send_message(message.from_user.id, 'Загрузка успешно завершена!', reply_markup=kb_admin)
    await state.finish()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('удалить '))
async def delete(callback : types.CallbackQuery):
    name = callback.data.split()[1]
    await del_info(name)
    await callback.answer('Позиция в меню успешно удалена!', show_alert=True)

@dp.message_handler(commands=['start'])
async def Help(message : types.message):
    if message.from_user.id == 5221868883:
        await message.delete()
        await bot.send_message(message.from_user.id, 'Добро пожаловать в бота нашей пиццерии Free Pizza!', reply_markup=kb_admin)
        await bot.send_message(message.from_user.id, HELP + '\n\nВы вошли как Администратор', reply_markup=kb_inline) 
    else:
        await message.delete()
        await bot.send_message(message.from_user.id, 'Добро пожаловать в бота нашей пиццерии Free Pizza!', reply_markup=kb_client)
        await bot.send_message(message.from_user.id, HELP, reply_markup=kb_inline)

@dp.message_handler(commands=['режим'])
@dp.message_handler(Text(equals=['режим'], ignore_case=True))
async def rejim(message : types.message):
    await message.reply(rej)

@dp.message_handler(commands=['место'])
@dp.message_handler(Text(equals=['место'], ignore_case=True))
async def ras(message : types.message):
    await message.reply(rasp)

@dp.message_handler(commands=['меню'])
@dp.message_handler(Text(equals=['меню'], ignore_case=True))
async def menu(message : types.message):
    await read_info(message.from_user.id)

@dp.callback_query_handler(text='меню')
async def call_menu(callback : types.CallbackQuery):
    await callback.message.answer('Меню Free Pizza:')
    await read_info(callback.from_user.id)
    await callback.answer()

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('заказать '))
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

@dp.message_handler(state=FSM_client.number)
async def num_zak(message : types.message, state : FSMContext):
    try:
        global dat
        dat.append(int(message.text))
        await message.reply('Как вас зовут?')
        await FSM_client.next()
    except:
        await message.reply('Введите корректный номер')
        FSMContext.reset()

@dp.message_handler(state=FSM_client.name)
async def name_zak(message : types.message, state : FSMContext):
    global dat, pizza
    dat.append(message.text)
    await bot.send_message(5221868883, f'@{message.from_user.username} заказал {pizza.lower()}\nТелефон: {dat[0]}\nИмя: {dat[1].capitalize()}')
    await state.finish()
    if message.from_user.id == 5221868883:
        await bot.send_message(message.from_user.id, f'{dat[1]}, вы успешно заказали пиццу!', reply_markup=kb_admin)
    else:
        await bot.send_message(message.from_user.id, f'{dat[1]}, Вы успешно заказали пиццу!', reply_markup=kb_client)

@dp.message_handler()
async def other(message : types.message):
    await message.reply('Команда не найдена!')

executor.start_polling(dp, skip_updates=True, on_startup=start_bot)
