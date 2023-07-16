from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from os import getenv

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)