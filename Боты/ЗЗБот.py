import telebot
token='5842840431:AAFb0wu467cu73N37ATvyPNd431NiFIjkKY'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def HELP(message):
    bot.send_message(message.chat.id, 'Отправь мне дату и месяц и я определю знак зодиака! Пример - 29 декабрь')
@bot.message_handler(content_types=['text'])
def default(message):
    command=message.text.split()
    if len(command)==2:
        mes=command[1].lower()
        try:
            date=int(command[0])
            if date>0 and date<32:
                if mes=='январь' or mes=='февраль' or mes=='март' or mes=='апрель' or mes=='май' or mes=='июнь' or mes=='июль' or mes=='август' or mes=='сентябрь' or mes=='октябрь' or mes=='ноябрь' or mes=='декабрь':
                    if mes=='январь':
                        if date<21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - козерог!')
                        elif date>20:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - водолей!')
                    elif mes=='февраль':
                        if date<21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - водолей!')
                        elif date>20 and date<30:
                            bot.send_message(message.chat.id,'Ваш знак зодиана - рыбы!')
                        else:
                            bot.send_message(message.chat.id,'Увы, но в феврале всего-то 29 дней!')
                    elif mes=='март':
                        if date<21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - рыбы!')
                        elif date>20:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - овен!')
                    elif mes=='апрель':
                        if date<21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - овен!')
                        elif date>20:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - телец!')
                    elif mes=='май':
                        if date<21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - телец!')
                        elif date>20:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - близнецы!')
                    elif mes=='июнь':
                        if date<22:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - близнецы!')
                        elif date>21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - рак!')
                    elif mes=='июль':
                        if date<23:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - рак!')
                        elif date>22:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - лев!')
                    elif mes=='август':
                        if date<24:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - лев!')
                        elif date>23:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - дева!')
                    elif mes=='сентябрь':
                        if date<24:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - дева!')
                        elif date>23:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - весы!')
                    elif mes=='октябрь':
                        if date<24:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - весы!')
                        elif date>23:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - скорпион!')
                    elif mes=='ноябрь':
                        if date<23:
                             bot.send_message(message.chat.id,'Ваш знак зодиака - скорпион!')
                        elif date>22:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - стрелец!')
                    elif mes=='декабрь':
                        if date<22:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - стрелец!')
                        elif date>21:
                            bot.send_message(message.chat.id,'Ваш знак зодиака - козерог!')
                else:
                    bot.send_message(message.chat.id, 'Неправильный месяц!')
            else:
                bot.send_message(message.chat.id, 'Неправильная дата!')
        except ValueError:
            bot.send_message(message.chat.id,'Введите корректную дату!')
    else:
        bot.send_message(message.chat.id, 'Введите только дату и число! Пример - 29 декабрь')
bot.polling(none_stop=True)
