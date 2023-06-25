while True:
    file = open('open\\text.txt', 'a')
    num = input('Текст: ')
    file.write(f'{num}\n')
    file.close()
    file = open('open\\text.txt', 'r')
    print(file.read())
    file.close()