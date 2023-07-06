while True:
    try:
        nums = '123456789'
        num = input('Введите целое число: ')
        if type(eval(num)) == int:
            for i in nums:
                counter = 0
                for n in num:
                    if i == n:
                        counter += 1
                if counter > 0:
                    print(f'В числе {num} цифра {i} повторяется {counter} раз(a)!')
        else:   
            raise ValueError()
    except:
        print('Irregular numbers!')