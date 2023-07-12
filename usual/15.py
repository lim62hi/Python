from random2 import randint
try:
    first = []
    second = []
    count = 0
    while count <= 5:
        count += 1
        first.append(randint(1, 11))
    while count <= 15:
        count += 1
        second.append(randint(11, 31))
    res = (first, second)
    print(res)
except:
    print('error')