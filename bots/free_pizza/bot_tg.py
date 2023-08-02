from aiogram.utils import executor
from create import dp
from handlers import admin, client, other
from data_base.sqlite_db import sq_start

async def start_bot(_):
    print('Бот включился и исправно работает!')

sq_start()
client.reg(dp)
admin.reg(dp)
other.reg(dp)

executor.start_polling(dp, skip_updates=True, on_startup=start_bot)