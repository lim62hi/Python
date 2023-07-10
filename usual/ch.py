from random2 import randint

def ind(array = None, index = None):
    if array != None and index != None:
        arr = []
        while index < len(array):
            arr.append(array[index])
            index += 2
        return arr
    else:
        return None

while True:
    try:
        le = int(input('Длина списка: '))
        array = []
        count = 0
        while count < le:
            count += 1
            array.append(randint(0, 1000))
        index_ch = 0
        index_nch = 1
        print(f'Изначально: {array} \nЧетные: {ind(array, index_ch)} \nНечетные: {ind(array, index_nch)}!')
    except ValueError:
        print('Irregular numbers!')
    except:
        print('error')