counter = 1
while True:
    try:
        with open('open\\text.txt', 'w') as file:
            numbers = input('Числа через пробел: ').split()
            numbers = [float(i) for i in numbers]
            file.write(f'{sum(numbers)}\n')
        with open('open\\text.txt', 'r') as file:
            result = file.read()
            print(f'{counter} результат: {result}')
            counter += 1
    except ValueError:
        print('Введите корректные числа!')