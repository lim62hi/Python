from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create import bot
from aiogram import types, Dispatcher
from keyboards.admin_kb import kb_admin, kb_onload

ID = None

class FSM_admin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

async def moder(message : types.message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что вы хотите сделать?', reply_markup=kb_admin)
    await message.delete()
    
async def load(message : types.message):
    if message.from_user.id == ID:
        await FSM_admin.photo.set()
        await bot.send_message(message.from_user.id, 'Начинаю загрузку', reply_markup=kb_onload)
        await message.reply('Загрузите фото')

async def load_photo(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSM_admin.next()
    await message.reply('Введите название')

async def load_name(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSM_admin.next()
    await message.reply('Введите описание')

async def load_description(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSM_admin.next()
    await message.reply('Введите цену')

async def load_price(message : types.message, state : FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await message.reply(str(data))
    await bot.send_message(message.from_user.id, 'Загрузка успешно завершена!', reply_markup=kb_admin)
    await state.finish()

async def cancel(message : types.message, state : FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, 'Загрузка отменена!', reply_markup=kb_admin)

def reg(dp : Dispatcher):
    dp.register_message_handler(moder, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(load, commands=['загрузить'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM_admin.photo)
    dp.register_message_handler(load_name, state=FSM_admin.name)
    dp.register_message_handler(load_description, state=FSM_admin.description)
    dp.register_message_handler(load_price, state=FSM_admin.price)
    dp.register_message_handler(cancel, commands=['отмена'], state='*')