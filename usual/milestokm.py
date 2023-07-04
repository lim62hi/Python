while True:
    try:
        mile = float(input('Сколько миль? '))
        km = mile * 1.6
        print(f'{mile} мил. равны {km} км.')
    except:
        print('Введите корректные числа!')