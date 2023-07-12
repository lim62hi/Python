while True:
    try:
        text = [i for i in input('Text: ').split()]
        text = list(set(text))
        print(f'Уникальные символы: {text}')
    except:
        print('error')