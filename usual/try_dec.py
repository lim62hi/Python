def tries(func):
    def wrapper():
        while True:
            try:
                func()
                break
            except:
                print('error')
    return wrapper

@tries
def a():
    numbers = input('Введите числа через пробел: ').split()
    numbers = [float(i) for i in numbers]
    print(f'Результат: {sum(numbers)}')

a()