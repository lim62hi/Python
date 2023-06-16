while True:
    try:
        x=int(input('Введите число: '))
        if x % 2 == 0:
            print('Четное')
        elif x % 2 == 1:
            print('Нечетное')
    except:
        print('Введите корректное число!')
