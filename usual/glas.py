while True:
    try:
        glas = 'ауоыиэяюеё'
        sogl = 'бвгджзйклмнпрстфхцчщш'
        nums = '123456789'
        text = [i for i in input('Text: ') if i != ' ']
        text = list(set(text))
        glas = [i for i in glas if i in text]
        sogl = [i for i in sogl if i in text]
        nums = [i for i in nums if i in text]
        dif = [i for i in text if i not in glas and i not in sogl and i not in nums]
        print(f'Список гласных: {glas}\nСписок согласных: {sogl}\nСписок цифр: {nums}\n\nДругие символы: {dif}')
    except:
        print('error')