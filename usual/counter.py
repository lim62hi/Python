while True:
    try:
        text = [i for i in input('Text: ') if i != ' ']
        dic = dict()
        letters = [i for i in 'ауоыиэяюеёбвгджзйклмнпрстфхцчщш123456789' if i in list(set(text))]
        count = 0
        for i in letters:
            dic[i] = text.count(i)
        print(dic)
    except:
        print('error')