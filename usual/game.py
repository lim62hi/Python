while True:
    try:
        count = 0
        res = eval(input('5 + 5 = '))
        if res == 10:
            count += 1
        res = eval(input('1 + 12.2 = '))
        if res == 13.2:
            count += 1
        res = eval(input('0 - 5 = '))
        if res == -5:
            count += 1
        print(f'Колличество правильных ответов: {count}')
    except ValueError:
        print('Irregular numbers!')
    except:
        print('error')