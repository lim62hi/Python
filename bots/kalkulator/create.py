from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from os import getenv

bot = Bot(getenv('TOKEN'))
dp = Dispatcher(bot)