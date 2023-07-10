from random2 import randint
while True:
    try:
        le = int(input('Длина списка: '))
        def gen(l = None):
            if l != None:
                array = []
                count = 0
                while count < le:
                    count += 1
                    array.append(randint(0, 10))
                return array
            else:
                return None
        print(gen(le))
    except:
        print('Error')