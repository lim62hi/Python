while True:
    try:
        num = int(input('До какого числа? '))
        nums = range(1, num + 1)
        three = [i for i in nums if i % 3 == 0 and i % 4 != 0]
        four = [i for i in nums if i % 4 == 0 and i % 3 != 0]
        print(f'{three}\n{four}')
    except ValueError:
        print('Irregular numbers!')
    except:
        print('error')