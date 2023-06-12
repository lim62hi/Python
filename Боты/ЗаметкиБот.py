import telebot
token='6011288732:AAHrY8oDYMwPootKa4EFfZ6EhZ9-J0Te0Co'
bot=telebot.TeleBot(token)
HELP="""/Помощь - команды и их описание (/Помощь)
/Добавить - добавить задачу (/Добавить "дата", "задача")
/Удалить - удалить задачу (/Удалить "дата", "задача")
/Задачи - посмотреть задачи, которые вы уже записали (/Задачи "дата")
/Все - показать все задачи (/Все)"""
tasks={}
@bot.message_handler(commands=['Помощь'])
def help(message):
    bot.send_message(message.chat.id, HELP)
@bot.message_handler(commands=['Добавить'])
def add(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=2)
    date=command[1]
    task=command[2]
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date]=[task]
    bot.send_message(message.chat.id, f'Задача "{task}" добавлена на дату "{date}"!')
@bot.message_handler(commands=['Удалить'])
def delete(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=2)
    date=command[1]
    task=command[2]
    if date in tasks:
        tasks[date].remove(task)
        bot.send_message(message.chat.id, 'Успешно удалено!')
    else:
        bot.send_message(message.chat.id, 'Увы, но такой задачи нет!')
@bot.message_handler(commands=['Задачи'])
def print_tasks(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=1)
    date=command[1]
    if date in tasks:
        bot.send_message(message.chat.id, f'Вы должны {date}:')
        for task in tasks[date]:
            bot.send_message(message.chat.id, f'- {task}')
    else:
        bot.send_message(message.chat.id, 'Увы, такой даты нет!')
@bot.message_handler(commands=['Все'])
def print_all(message):
    for date in tasks:
        bot.send_message(message.chat.id, f'Вы должны {date}:')
        for task in tasks[date]:
            bot.send_message(message.chat.id, f'- {task}')
@bot.message_handler(commands=['помощь'])
def help(message):
    bot.send_message(message.chat.id, HELP)
@bot.message_handler(commands=['добавить'])
def add(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=2)
    date=command[1]
    task=command[2]
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date]=[task]
    bot.send_message(message.chat.id, f'Задача "{task}" добавлена на дату "{date}"!')
@bot.message_handler(commands=['удалить'])
def delete(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=2)
    date=command[1]
    task=command[2]
    if date in tasks:
        tasks[date].remove(task)
        bot.send_message(message.chat.id, 'Успешно удалено!')
    else:
        bot.send_message(message.chat.id, 'Увы, но такой задачи нет!')
@bot.message_handler(commands=['задачи'])
def print_tasks(message):
    mes=message.text.lower()
    command=mes.split(maxsplit=1)
    date=command[1]
    if date in tasks:
        bot.send_message(message.chat.id, f'Вы должны {date}:')
        for task in tasks[date]:
            bot.send_message(message.chat.id, f'- {task}')
    else:
        bot.send_message(message.chat.id, 'Увы, такой даты нет!')
@bot.message_handler(commands=['все'])
def print_all(message):
    for date in tasks:
        bot.send_message(message.chat.id, f'Вы должны {date}:')
        for task in tasks[date]:
            bot.send_message(message.chat.id, f'- {task}')
bot.polling(none_stop=True)
