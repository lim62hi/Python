while True:
    try:
        nums = [float(i) for i in input('Two numbers: ').split()]
        def ur(a = None, b = None):
            if a != None and b != None:
                x = b - 1 / a - 1 if a != 0 else None
                return x
            else:
                return None
        print(ur(nums[0], nums[1]))
    except ValueError:
        print('Irregular numbers!')
    except:
        print('Error')