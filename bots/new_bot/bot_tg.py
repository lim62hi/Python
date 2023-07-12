import aiogram as aio
import os, json, string

bot = aio.Bot(token=os.getenv('TOKEN'))
dp = aio.dispatcher.Dispatcher(bot)
HELP = '''/help - список команд
/work - режим работы
/location - расположение кафе

Приятного аппетита!'''
rej = 'Режим работы: любой день недели 8:00 - 20:00'
rasp = 'Улица Колбасная 15А'
ls = 'Пожалуйста, напишите мне в личные сообщения, чтобы я мог с Вами общаться через них и присылать Вам личную информацию!'

async def start_bot(_):
    print('Бот включился и исправно работает!')

@dp.message_handler(commands=['start', 'help'])
async def Help(message : aio.types.message):
    try:
        await bot.send_message(message.from_user.id, HELP)
        await message.delete()
    except:
        await message.reply(f'{HELP}\n\n{ls}')

@dp.message_handler(commands=['work'])
async def rejim(message : aio.types.message):
    try:
        await bot.send_message(message.from_user.id, rej)
        await message.delete()
    except:
        await message.reply(f'{rej}\n\n{ls}')

@dp.message_handler(commands=['location'])
async def ras(message : aio.types.message):
    try:
        await bot.send_message(message.from_user.id, rasp)
        await message.delete()
    except:
        await message.reply(f'{rasp}\n\n{ls}')

@dp.message_handler()
async def ban_word(message : aio.types.message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}\
    .intersection(set(json.load(open('words.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()



aio.utils.executor.start_polling(dp, skip_updates=True, on_startup=start_bot)