from module import hello as h
print(h(input('Введите ваше имя: ')))
while True:
    try:
        numbers = input('Числа через пробел: ').split()
        numbers = [float(i) for i in numbers]
        with open('open\\text.txt', 'r') as file:
            counter = int(file.read())
        print(f'{counter} результат: {sum(numbers)}')
        counter += 1
        with open('open\\text.txt', 'w') as file:
            file.write(f'{counter}')
    except ValueError:
        print('Введите корректные числа!')