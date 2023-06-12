HELP="""Помощь - команды и их описание
Добавить - добавить задачу
Удалить - удалить задачу
Задачи - посмотреть задачи, которые вы уже записали
"""
tasks={}
print(HELP)
while True:
    command=input('Какую команду вы хотите исполнить? ')
    command=command.lower()
    if command=='помощь':
        print(HELP)
    elif command=='удалить':
        date=input('На какую дату вы хотите удалить задачу? ')
        task=input('Задача, которую вы хотите удалить: ')
        if date in tasks and task in tasks[date]:
            tasks[date].remove(task)
            print('Задача успешно удалена!')
        else:
            print('Неверная дата/задача!')
    elif command=='добавить':
        task=input('Что вы хотите сделать? ')
        date=input('Когда? ')
        date=date.lower()
        task=task.lower()
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]
        print('Задача добавлена!')
    elif command=='задачи':
        date=input('На какое число посмотрим задачи? ')
        date=date.lower()
        if date in tasks:
            l=len(tasks[date])
            print('Вы должны: ')
            for task in tasks[date]:
                print(f'- {task}')
        else:
            print('Увы, но такой даты нет!')
    else:
        print('Введите корректную команду!')
