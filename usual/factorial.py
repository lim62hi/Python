while True:
    try:
        num = int(input('Введите число: '))
        if num > 0:
            nums = list(range(1, num + 1))
            first = nums[0]
            nums.pop(0)
            nums = [i*first for i in nums]
            fac = sum(nums)
            print(f'Факториал: {fac}')
        else:
            print('Факториал отрицательного числа или нуля нельзя вычислить!')
    except:
        print('Введите корректные числа!')