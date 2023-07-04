while True:
    try:
        num = int(input('Введите число: '))
        if num % 3 != 0:
            print('Число делится на 3 не нацело!')
        elif num % 3 == 0:
            print('Число делится на 3 нацело!')
    except:
        print('Введите корректные числа!')