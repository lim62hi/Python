while True:
    try:
        nums = input('Numbers: ').split()
        nums = [int(i) for i in nums]
        count = -1
        for i in nums:
            count += 1
            if i < 10:
                dop = 9 - i
                nums[count] = dop
                print(f'Цифре {i} до цифры 9 нужно еще {dop}')
            else:
                dop = i - 9
                nums[count] = dop
                print(f'Цифра {i} больше цифры 9 на {dop}')       
    except ValueError:
        print('Irregular numbers')