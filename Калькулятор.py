while True:
    x=input('Введите действие: ')
    x=x.lower()
    if x=='сложить' or x=='отнять' or x=='умножить' or x=='разделить':
        try:
            y=float(input('Первое число: '))
            z=float(input('Второе число: '))
            if x == 'сложить':
                r=y+z
                print(f'Результат: {r}')
            elif x== 'отнять':
                r=y-z
                print(f'Результат: {r}')
            elif x=='разделить':
                try:
                    r=y/z
                    print(f'Результат: {r}')
                except ZeroDivisionError:
                    print('Увы, но делить на ноль нельзя!')
            elif x=='умножить':
                r=y*z
                print(f'Результат: {r}')
            else:
                print('Увы, но такого действия нет!')
        except ValueError:
            print('Введите корректные числа!')
    else:
        print('Сложить, отнять, разделить или умножить?')
    
