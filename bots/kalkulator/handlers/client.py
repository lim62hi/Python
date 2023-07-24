from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create import bot
from keyboards.client_kb import kb_user, kb_cancel
from handlers.other import Help
from aiogram.dispatcher.filters import Text

text = None

HELP = '''Привет!

В этом боте ты с легкостью можешь выполнять простые математические действия: сложение, вычитание, умножение и деление

Чтобы воспользоваться ботом выбери нужную тебе кнопку на клавиатуре!'''

class FSM_res(StatesGroup):
    result = State()

async def help_start(message : types.message):
    await bot.send_message(message.from_user.id, HELP, reply_markup=kb_user)
    await message.delete()

async def enter(message : types.message):
    await FSM_res.result.set()
    global text 
    text = message.text.lower()
    if '/' not in text:
        text = '/' + text
    if text == '/сложить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите сложить', reply_markup=kb_cancel)
    elif text == '/вычесть':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите вычесть', reply_markup=kb_cancel)
    elif text == '/умножить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите умножить', reply_markup=kb_cancel)
    elif text == '/разделить':
        await bot.send_message(message.from_user.id, 'Введите числа, которые вы хотите разделить', reply_markup=kb_cancel)
    elif text == '/пример':
        await bot.send_message(message.from_user.id, 'Введите пример, который вы хотите решить', reply_markup=kb_cancel)

async def cancel(message : types.message, state : FSMContext):
    now = state.get_state()
    if now is None:
        Help()
    await state.finish()
    await bot.send_message(message.from_user.id, 'Операция отменена!', reply_markup=kb_user)

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

def reg(dp : Dispatcher):
    dp.register_message_handler(help_start, commands=['start'])
    dp.register_message_handler(enter, commands=['сложить', 'вычесть', 'умножить', 'разделить', 'пример'], state=None)
    dp.register_message_handler(enter, Text(equals=['сложить', 'вычесть', 'умножить', 'разделить', 'пример'], ignore_case=True), state=None)
    dp.register_message_handler(cancel, commands=['отмена'], state='*')
    dp.register_message_handler(cancel, Text(equals=['отмена'], ignore_case=True), state='*')
    dp.register_message_handler(result, state=FSM_res.result)