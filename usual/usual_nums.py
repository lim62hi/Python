while True:
    try:
        ir_nums = [int(i) for i in input('Недопустимые числа: ').split()]
        und = int(input('До скольки? '))
        nums = []
        for i in range(1, und + 1):
            if i not in ir_nums:
                nums.append(i)
        print(f'Сумма чисел в списке: {sum(nums)}')
    except ValueError:
        print('Irregular values!')