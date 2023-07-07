while True:
    try:
        def tre(a = None, b = None, c = None):
            if a != None and b != None and c != None:
                if a == b == c: 
                    return 'Равносторонний'
                elif a != b != c:
                    return 'Разносторонний'
                else:
                    return 'Равнобедренный'
            else:
                return None
        nums = [float(i) for i in input('Числа: ').split()]
        print(f'Ваш треугольник {tre(nums[0], nums[1], nums[2])}')
    except:
        print('Error')