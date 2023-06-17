while True:
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    text = input('Введите слово, чтобы подсчитать буквы: ')
    for i in letters:
        if i in text:
            print(f'В тексте есть {text.count(i)} {i}')