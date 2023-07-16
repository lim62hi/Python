from aiogram.utils import executor
from create import dp
from handlers import admin, client, other

async def start_bot(_):
    print('Бот включился и исправно работает!')

client.reg(dp)
other.reg(dp)

executor.start_polling(dp, skip_updates=True, on_startup=start_bot)