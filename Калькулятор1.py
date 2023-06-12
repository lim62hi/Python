while True:
    def minus(znach, znach1):
        znach-=znach1
        return znach
    def plus(znach, znach1):
        znach+=znach1
        return znach
    def delen(znach, znach1):
        try:
            znach/=znach1
            return znach
        except ZeroDivisionError:
            znach='делить на ноль нельзя'
            return znach
    def umnoj(znach, znach1):
        znach*=znach1
        return znach
    def total ():
        try:
            x=float(input('Первое число: '))
            x1=float(input('Второе число: '))
            print(f'Разность: {minus(x,x1)}')
            print(f'Сумма: {plus(x,x1)}')
            print(f'Деление: {delen(x,x1)}')
            print(f'Умножение: {umnoj(x,x1)}')
        except ValueError:
            print('Введите корректные числа!')
    total()
