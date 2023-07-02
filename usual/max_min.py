def minimal(*massive):
    min = massive[0]
    max = massive[0]
    for number in massive:
        if min > number:
            min = number
    for number in massive:
        if max < number:
            max = number
    return min, max
res = minimal(1, 2, 100, 0)
print(f'Минимальное: {res[0]} \nМаксимальное: {res[1]}')