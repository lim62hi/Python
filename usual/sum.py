while True:
    try:
        nums = input('Numbers: ').split()
        nums = [int(i) for i in nums]
        def _sum_(array):
            arraych = [i for i in array if i % 2 == 0]
            arrayne = [i for i in array if i % 2 == 1]
            nech = sum(arrayne)
            ch = sum(arraych)
            return nech, ch
        res = _sum_(nums)
        print(f'Сумма нечетных: {res[0]}, сумма четных {res[1]}!')
    except:
        print('Irregular numbers!')