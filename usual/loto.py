from random import randint
while True:
    loto = input('В какое лото вы хотите поиграть? Справка: 4/20, 5/36, 6/45, 7/49\n')
    if loto == '4/20':
        nums1 = [int(i) for i in input('Введите 4 числа: ').split()]
        nums2 = []
        count = 0
        while count <= 4:
            count += 1
            num = randint(1, 21)
            print(num)
    elif loto == '5/36':
        pass
    elif loto == '6/45':
        pass
    elif loto == '7/49':
        pass
    else:
        print('Я не знаю такого лото!')