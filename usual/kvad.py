while True:
    try:
        num = int(input('Степени какого числа вы хотите увидеть? '))
        times = int(input('Сколько степеней вы хотите увидеть? '))
        for step in range(2,times + 1):
            print(f'{num**step} - {num} в степени {step}')
    except:
        print('Введите корректные числа!')