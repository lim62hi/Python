from random import randint
def con():
    cont = 0
    for num in nums1:
        if num in nums2:
            cont +=1
    return cont
def get_your():
    for num in sorted(nums1):
        print(num)
def get_our():
    for num in sorted(nums2):
        print(num)
def info():
    print('Ваши цифры:')
    get_your()
    print('Наши цифры:')
    get_our()
while True:
    loto = input('В какое лото вы хотите поиграть? Справка: 4/20, 6/36, 7/49\n')
    try:
        if loto == '4/20':
            nums1 = [int(i) for i in input('Введите 4 числа: ').split()]
            nums2 = []
            count = 0
            while len(nums2) != 4:
                num = randint(1, 20)
                if num not in nums2:
                    nums2.append(num)
            if len(nums1) > 4:
                    raise SyntaxError
            elif len(nums1) < 4:
                    raise KeyError
            for num in nums1:
                if num < 1 or num > 20:
                    raise ValueError
                else:
                    if num in nums2:
                        count += 1
            if count == 4:
                print('Вы выйграли! Угаданы 4/4 цифр!')
                info()
            else:
                print(f'Вы проиграли! Угадано {con()} цифр(ы)')
                info()
        elif loto == '6/36':
            nums1 = [int(i) for i in input('Введите 6 чисел: ').split()]
            nums2 = []
            count = 0
            while len(nums2) != 6:
                num = randint(1, 36)
                if num not in nums2:
                    nums2.append(num)
            if len(nums1) > 6:
                    raise SyntaxError
            elif len(nums1) < 6:
                    raise KeyError
            for num in nums1:
                if num < 1 or num > 36:
                    raise ValueError
                else:
                    if num in nums2:
                        count += 1
            if count == 6:
                print('Вы выйграли! Угаданы 6/6 цифр!')
                info()
            else:
                print(f'Вы проиграли! Угадано {con()} цифр(ы)')
                info()
        elif loto == '7/49':
            nums1 = [int(i) for i in input('Введите 7 чисел: ').split()]
            nums2 = []
            count = 0
            while len(nums2) != 7:
                num = randint(1, 49)
                if num not in nums2:
                    nums2.append(num)
            if len(nums1) > 7:
                    raise SyntaxError
            elif len(nums1) < 7:
                    raise KeyError
            for num in nums1:
                if num < 1 or num > 49:
                    raise ValueError
                else:
                    if num in nums2:
                        count += 1
            if count == 7:
                print('Вы выйграли! Угаданы 7/7 цифр!')
                info()
            else:
                print(f'Вы проиграли! Угадано {con()} цифр(ы)')
                info()
        else:
            print('Я не знаю такого лото!')
    except ValueError:
        print('Неправильные числа!')
    except SyntaxError:
        print('Слишком много чисел!')
    except KeyError:
        print('Слишком мало чисел!')