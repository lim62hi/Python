def count1(letter, massive):
    try:
        counter = 0
        for i in massive:
            if letter == i:
                counter += 1
    except:
        counter = 'Неправильные аргументы'
    return counter

letters = ('a', 1, 'a')
print(count1('b', letters))