while True:
    try:
        text = input('Введите текст: ').split()
        new = text[0]
        text.pop(0)
        for i in text:
            new += i
        print(f'Ваш новый текст: {new}')
    except:
        print('Irregular text!')