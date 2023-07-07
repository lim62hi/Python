while True:
    try:
        nums = [float(i) for i in input('Numbers: ').split()]
        def arif(arr = None):
            if arr != None and len(arr) > 1:
                dop = arr[1] - arr[0]
                last = arr[0]
                arr.pop(0)
                for i in arr:
                    if last + dop == i:
                        last = i
                        res =  True
                    else:
                        res = False
                return res
            else:
                return None
        print(f'Арифметическая последовательность? {arif(nums)}')
    except ValueError:
        print('Irregular numbers!')
    except:
        print('Error')