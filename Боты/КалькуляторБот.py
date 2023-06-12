import telebot
import math
import decimal
token='6246734881:AAEqTBJvqVniNBxPHvS5WfG-AX4m7bRRNAM'
bot=telebot.TeleBot(token)
HELP="""• Привет! Введи несколько чисел, с ними выполнятся простые действия: плюс, минус, умножить, разделить! 
• Если же ты введешь одно число, оно возведется в квадрат и куб, а так же из него вычислится квадратный корень!

• /start для того, чтобы вывести меню еще раз"""
@bot.message_handler(commands=['start'])
def Help(message):
    bot.send_message(message.chat.id, HELP)
@bot.message_handler(content_types=['text'])
def all(message):
    try:
        command=[decimal.Decimal(i) for i in message.text.split()]
        if len(command)>1:
            com=[i for i in command]
            com.pop(0)
            plus=0
            for i in command:
                plus+=i
            summa=0
            for i in com:
                summa+=i
            num=command[0]
            for index in range(1, len(command)):
                try:
                    num/=command[index]
                except ZeroDivisionError:
                    num='делить на ноль нельзя'
            bot.send_message(message.chat.id, f'Сложить: {plus}')
            bot.send_message(message.chat.id, f'Вычесть: {command[0]-summa}')
            bot.send_message(message.chat.id, f'Умножить: {math.prod(command)}')
            bot.send_message(message.chat.id, f'Разделить: {num}')
        elif len(command)==1:
            command=message.text.split()
            num=decimal.Decimal(command[0])
            bot.send_message(message.chat.id, f'Квадрат: {num**2}')
            bot.send_message(message.chat.id, f'Куб: {num**3}')
            bot.send_message(message.chat.id, f'Квадратный корень: {decimal.Decimal(math.sqrt(num))}')
    except:
        bot.send_message(message.chat.id, 'Введите корректные числа!')
bot.polling(none_stop=True)
