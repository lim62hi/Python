import aiogram as ai
import os

bot = ai.Bot(token=os.getenv('TOKEN'))
dp = ai.dispatcher.Dispatcher(bot)

@dp.message_handler()
async def echo(message : ai.types.message):
    if message.text.lower() == 'привет':
        await message.reply('И тебе привет!')
    elif message.text.lower() == 'как дела':
        await message.reply('Отлично, а у тебя?')
    else:
        #await message.answer(message.text)
        await message.reply(message.text)
        #await bot.send_message(message.from_user.id, message.text)



ai.utils.executor.start_polling(dp, skip_updates=True)