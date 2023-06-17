while True:
    try:
        time = int(input('Введите количество секунд: '))
        days = time // 86400
        time %= 86400
        hours = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        print(f'{days} день:{hours} часов:{minutes} минут:{time} секунд')
    except:
        print('Введите корректное число!')