print('Для справки: алкоголь, хлеб, вода')
while True:
    x=input('Что вы хотите купить? ')
    if x == 'алкоголь':
        i=input('Вам есть 18 лет? ')
        if i == 'да':
            print('Хорошо, мы продадим вам его!')
        elif i == 'нет':
            print('Иди вон из магазина! Ты пытался купить алкоголь зная, что тебе нет 18 лет, таким образом, ты пытался меня обмануть!')
            break
        else:
            print('Иди вон из магазина! Ты даже да или нет ответить не можешь, ты и так уже бухой!')
            break
    elif x == 'хлеб':
        i=input('У вас есть 40 рублей? ')
        if i == 'да':
            print('Хорошо, мы продадим вам его')
        elif i == 'нет':
            print('40 рублей на хлеб нет? Позор! Ладно, внучек, пробью тебе хлеб за мой счет, ступай с богом!')
            break
        else:
            print('Свяжи свои слова нормально и приходи потом!')
            break
    elif x == 'вода':
        i==input('У вас есть 20 рублей на воду? ')
        if i == 'да':
            print('Хорошо, мы продадим вам водички!')
        elif i == 'нет':
            print('Нет так нет. Не продам я вам, иди отсюда!')
            break
        else:
            print('Можешь связать свои слова нормально?')
            break
    else:
        print('Свяжи слова свои нормально!')
