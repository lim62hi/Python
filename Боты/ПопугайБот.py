import telebot
token='6033680967:AAGYMLo9hunaPQFDBxExBmECmle9V4cGtPU'
bot=telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(none_stop=True)
