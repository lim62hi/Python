from aiogram.utils import executor
from create import dp
from handlers import client, other

async def startbot(_):
    print('Бот включился и исправно работает!')

client.reg(dp)
other.reg(dp)

executor.start_polling(dp, skip_updates=True, on_startup=startbot)