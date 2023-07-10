def maxes(arr = None):
    if arr != None:
        min_arr = []
        counter = -1
        while counter <= len(arr):
            counter += 1
            if min(arr) not in min_arr:
                min_arr.append(min(arr))
            arr.remove(min(arr))
        max_arr = min_arr.copy()
        max_arr.reverse()
        return min_arr, max_arr
    else:
        return None
while True:
    try:
        array = [float(i) for i in input('Numbers: ').split()]
        res = maxes(array)
        print(f'Min to max: {res[0]} \nMax to min: {res[1]}')
    except ValueError:
        print('Irregular numbers!')
    except:
        print('Error')