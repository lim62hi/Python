while True:
    text = input('Введите тект: ').split(', ')
    hobbies = [i.capitalize() for i in text]
    hobbies = ', '.join(hobbies)
    print(hobbies)