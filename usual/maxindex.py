while True:
    try:
        nums = [float(i) for i in input('Numbers: ').split()]
        ma = max(nums)
        ma_index = nums.index(ma)
        print(f'{ma} - максимальный элемент, {ma_index} - индекс максимального элемента!')
    except:
        print('Error')