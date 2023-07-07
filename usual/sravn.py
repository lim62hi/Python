while True:
    try:
        arr = [int(i) for i in input('First numbers: ').split()]
        _arr_ = [int(i) for i in input('Second numbers: ').split()]
        def sravn(arr1 = None, arr2 = None):
            if arr1 != None and arr2 != None:
                if len(arr1) == len(arr2):
                    count = -1
                    for i in arr1:
                        count += 1
                        if i == arr2[count]:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return None
        print(f'Равны? {sravn(arr, _arr_)}')
    except:
        print('Error')