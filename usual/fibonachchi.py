while True:
    try:
        num = int(input('Сколько чисел вы хотите увидеть? '))
        counter = 2
        res = 0
        if num > 0:
            massive = [1, 1]
            if num == 1:
                print(1)
            elif num == 2:
                print(1, 1)
            else:
                while counter < num:
                    counter += 1
                    res = massive[-1] + massive[-2]
                    massive.append(res)
                for i in massive:
                    print(i, end=' ')
                print()
                    
        else:
            print('Введите положительное число!')
    except:
        print('Введите корректные числа!')