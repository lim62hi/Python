from random import randint

def con():
    cont = 0
    for num in nums1:
        if num in nums2:
            cont +=1
    return cont
def info(right):
    print('Вы угадали цифры: ')
    if right != []:
        for i in sorted(right):
            print(i)
    else:
        print(0)
    print('Ваши цифры:')
    for number in sorted(nums1):
        print(number)
    print('Наши цифры:')
    for number in sorted(nums2):
        print(number)
    print('\n\n\n')
def start_lot(num):
    global nums1, nums2
    nums1 = [int(i) for i in input(f'Введите {num} чисел(ла): ').split()]
    nums2 = []
    count = 0
    right = []
    if num == 4:
        lot = 20
    elif num == 6:
        lot = 36
    else:
        lot = 49
    while len(nums2) != num:
        numb = randint(1, lot)
        if numb not in nums2:
            nums2.append(numb)
    if len(nums1) > num:
        raise SyntaxError
    elif len(nums1) < num:
        raise KeyError
    for num in nums1:
        if num < 1 or num > lot:
            raise ValueError
        else:
            if num in nums2:
                count += 1
                right.append(num)
    if count == num:
        print(f'Вы выйграли! Угаданы {count}/{num} цифр!\n')
        info(right)
    else:
        print(f'Вы проиграли! Угадано {con()} цифр(ы)\n')
        info(right)
while True:
    loto = input('В какое лото вы хотите поиграть? Справка: 4/20, 6/36, 7/49\n')
    try:
        if loto == '4/20':
            start_lot(4)
        elif loto == '6/36':
            start_lot(6)
        elif loto == '7/49':
            start_lot(7)
        else:
            print('Я не знаю такого лото!')
    except ValueError:
        print('Неправильные числа!')
    except SyntaxError:
        print('Слишком много чисел!')
    except KeyError:
        print('Слишком мало чисел!')
    except:
        print('Возникла ошибка!')