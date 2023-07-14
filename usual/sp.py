while True:
    try:
        def sp(num = None):
            if num != None:
                if num < 1:
                    raise ValueError()
                else:
                    ar = [i for i in range(1, num + 1)]
                    dic_ar = dict()
                    fir = 0
                    las = -1
                    while fir < len(ar):
                        dic_ar[ar[fir]] = ar[las]
                        fir += 1
                        las -= 1
                    return dic_ar
            else:
                return None
        result = {**sp(int(input('Положительное число: '))), **sp(int(input('Положительное число: ')))}
        print(f'Result: {result}')
    except ValueError:
        print('Irregular Numbers')
    except:
        print('error')