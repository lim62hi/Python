from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint

number = None
bot = Bot(token='6182305853:AAGxLIaLK0hN0du8H0_7kF4wmu_bQ7U-WZk')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
HELP = 'Привет!\n\nВ этом боте вы можете поиграть в спортлото и обязательно выйграть миллион, а также автомобиль!\nВыберите лото, в которое вы хотите поиграть!'
class FSM_num(StatesGroup):
    result = State()
kb_start = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('4/20')).row(KeyboardButton('6/36'), KeyboardButton('7/49'))
leave = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Отмена'))

def con(nums1, nums2):
    cont = 0
    for num in nums1:
        if num in nums2:
            cont +=1
    return cont
async def info(right, nums1, nums2, message):
    ans = ans1 = ans2 = ''
    if right != []:
        for i in sorted(right):
            ans += f'{i} '
    else:
        ans = 'ничего'
    for number in sorted(nums1):
        ans1 += f'{number} '
    for number in sorted(nums2):
        ans2 += f'{number} '
    await message.answer(f'Вы угадали цифры: {ans}\n\nВаши цифры: {ans1}\nНаши цифры: {ans2}')
async def start_lot(num, nums1, message):
    nums2 = []
    count = 0
    right = []
    if num == 4:
        lot = 20
    elif num == 6:
        lot = 36
    else:
        lot = 49
    while len(nums2) != num:
        numb = randint(1, lot)
        if numb not in nums2:
            nums2.append(numb)
    if len(nums1) > num:
        await message.reply('Вы ввели слишком много чисел!')
        return
    elif len(nums1) < num:
        await message.reply('Вы ввели слишком мало чисел!')
        return
    elif len(list(set(nums1))) < 4:
        await message.reply('Вы ввели одинаковые числа!')
        return
    for num in nums1:
        if num < 1 or num > lot:
            await message.reply('Вы ввели неправильные числа чисел!')
            return
        else:
            if num in nums2:
                count += 1
                right.append(num)
    if count == num:
        await message.reply(f'Вы выйграли! Угаданы {count}/{num} цифр!\n')
        await info(right, nums1, nums2, message)
    else:
        await message.reply(f'Вы проиграли! Угадано {con(nums1, nums2)} цифр(ы)\n')
        await info(right, nums1, nums2, message)

async def onstart(_):
    print('Bot successfully started his work!')
async def ondown(_):
    print('Bot successfully ended his work!')

@dp.message_handler(commands=['start'])
async def start(message : types.message):
    await message.delete()
    await bot.send_message(message.from_user.id, HELP, reply_markup=kb_start)

@dp.message_handler(Text(equals=['4/20', '6/36', '7/49'], ignore_case=True), state=None)  
async def l_start(message : types.message):
    global number
    if number == None:
        number = int(message.text[0])
    await bot.send_message(message.from_user.id, f'ЛОТО НАЧАЛОСЬ! Введите {number} числа(ел)', reply_markup=leave)
    await FSM_num.result.set()

@dp.message_handler(commands=['отмена'], state='*')
@dp.message_handler(Text(equals=['отмена'], ignore_case=True), state='*')
async def cancel(message : types.message, state : FSMContext):
    await state.finish()
    await bot.send_message(message.from_user.id, 'Лото отменено!', reply_markup=kb_start)    

@dp.message_handler(state=FSM_num.result)
async def start_l(message : types.message, state : FSMContext):
    global number
    await start_lot(number, [int(i) for i in message.text.split()], message)
    await state.finish()
    await l_start(message)

@dp.message_handler()
async def other(message : types.message):
    await message.answer('Я не знаю такого лото!')

executor.start_polling(dp, skip_updates=True, on_startup=onstart, on_shutdown=ondown)