from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

storage = MemoryStorage()
bot = Bot(token='6246734881:AAEqTBJvqVniNBxPHvS5WfG-AX4m7bRRNAM')
dp = Dispatcher(bot, storage=storage)
text = None
HELP = '''Команда не найдена!

Выбери на клавиатуре то, что ты хочешь сделать'''
HELP = '''В этом боте ты с легкостью можешь выполнять простые математические действия: сложение, вычитание, умножение и деление, а также ты можешь решить свой пример!

Чтобы воспользоваться ботом выбери нужную тебе кнопку на клавиатуре!'''
HELP1 = '''На клавиатуре есть кнопки. После нажатия любой кнопки тебя
попросят ввести числа, с которыми ты хочешь сделать действие,
или же ты можешь отменить его.'''
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))
kb_user = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Пример')).row(KeyboardButton('Сложить'), KeyboardButton('Вычесть')).row(KeyboardButton('Умножить'), KeyboardButton('Разделить'))
kb_inline = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Помощь', callback_data='помощь'))

async def startbot(_):
    print('Бот включился и исправно работает!')

class FSM_res(StatesGroup):
    result = State()

@dp.message_handler(commands=['start'])
async def help_start(message : types.message):
    await message.delete()
    await bot.send_message(message.from_user.id, 'Привет!', reply_markup=kb_user)
    await bot.send_message(message.from_user.id, HELP, reply_markup=kb_inline)

@dp.message_handler(commands=['сложить', 'вычесть', 'умножить', 'разделить', 'пример'], state=None)
@dp.message_handler(Text(equals=['сложить', 'вычесть', 'умножить', 'разделить', 'пример'], ignore_case=True), state=None)
async def enter(message : types.message):
    await FSM_res.result.set()
    global text 
    text = message.text.lower()
    if '/' not in text:
        text = '/' + text
    if text == '/сложить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите сложить через пробел', reply_markup=kb_cancel)
    elif text == '/вычесть':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите вычесть через пробел', reply_markup=kb_cancel)
    elif text == '/умножить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите умножить через пробел', reply_markup=kb_cancel)
    elif text == '/разделить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите разделить через пробел', reply_markup=kb_cancel)
    elif text == '/пример':
        await bot.send_message(message.from_user.id, 'Введите пример, который вы хотите решить', reply_markup=kb_cancel)

@dp.message_handler(commands=['отмена'], state='*')
@dp.message_handler(Text(equals=['отмена'], ignore_case=True), state='*')
async def cancel(message : types.message, state : FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, 'Операция отменена!', reply_markup=kb_user)

@dp.message_handler(state=FSM_res.result)
async def result(message : types.message, state : FSMContext):
    global text
    while True:
        try:
            if text == '/пример':
                res = eval(message.text)
                await bot.send_message(message.from_user.id, f'Результат примера: {res}', reply_markup=kb_user)
            else:
                numbers = [float(i) for i in message.text.split()]
                res = numbers[0]
                numbers.pop(0)
                if text == '/сложить':
                    for i in numbers:
                        res += i
                    await bot.send_message(message.from_user.id, f'Результат сложения: {res}', reply_markup=kb_user)
                elif text == '/вычесть':
                    for i in numbers:
                        res -= i
                    await bot.send_message(message.from_user.id, f'Результат вычитания: {res}', reply_markup=kb_user)
                elif text == '/умножить':
                    for i in numbers:
                        res *= i
                    await bot.send_message(message.from_user.id, f'Результат умножения: {res}', reply_markup=kb_user)
                elif text == '/разделить':
                    for i in numbers:
                        res /= i
                    await bot.send_message(message.from_user.id, f'Результат деления: {res}', reply_markup=kb_user)
        except ZeroDivisionError:
            await message.reply('Делить на ноль нельзя!')
            await state.reset()
        except:
            await message.reply('Введите корректные числа!')
            await state.reset()
        else:
            await state.finish()
            break

@dp.callback_query_handler(text='помощь')
async def prim(callback : types.CallbackQuery):
    await callback.answer(HELP1, show_alert=True)

@dp.message_handler()
async def Help(message : types.message):
    await message.reply(HELP)

executor.start_polling(dp, skip_updates=True, on_startup=startbot)