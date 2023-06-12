print('Сейчас я определю ваш знак зодиака!')
while True:
    print('')
    mes1=input('В каком месяце вы родились? ')
    chis=input('Угу... А какого числа? ')
    try:
        chiss=int(chis)
        mes=mes1.lower()
        if chiss>0 and chiss<32:
            if mes=='январь':
                if chiss<21:
                    print('Ваш знак зодиака - козерог!')
                elif chiss>20:
                    print('Ваш знак зодиака - водолей!')
            elif mes=='февраль':
                if chiss<21:
                    print('Ваш знак зодиака - водолей!')
                elif chiss>20 and chiss<30:
                    print('Ваш знак зодиана - рыбы!')
                else:
                    print('Увы, но в феврале всего-то 29 дней!')
            elif mes=='март':
                if chiss<21:
                    print('Ваш знак зодиака - рыбы!')
                elif chiss>20:
                    print('Ваш знак зодиака - овен!')
            elif mes=='апрель':
                if chiss<21:
                    print('Ваш знак зодиака - овен!')
                elif chiss>20:
                    print('Ваш знак зодиака - телец!')
            elif mes=='май':
                if chiss<21:
                    print('Ваш знак зодиака - телец!')
                elif chiss>20:
                    print('Ваш знак зодиака - близнецы!')
            elif mes=='июнь':
                if chiss<22:
                    print('Ваш знак зодиака - близнецы!')
                elif chiss>21:
                    print('Ваш знак зодиака - рак!')
            elif mes=='июль':
                if chiss<23:
                    print('Ваш знак зодиака - рак!')
                elif chiss>22:
                    print('Ваш знак зодиака - лев!')
            elif mes=='август':
                if chiss<24:
                    print('Ваш знак зодиака - лев!')
                elif chiss>23:
                    print('Ваш знак зодиака - дева!')
            elif mes=='сентябрь':
                if chiss<24:
                    print('Ваш знак зодиака - дева!')
                elif chiss>23:
                    print('Ваш знак зодиака - весы!')
            elif mes=='октябрь':
                if chiss<24:
                    print('Ваш знак зодиака - весы!')
                elif chis>23:
                    print('Ваш знак зодиака - скорпион!')
            elif mes=='ноябрь':
                if chiss<23:
                    print('Ваш знак зодиака - скорпион!')
                elif chiss>22:
                    print('Ваш знак зодиака - стрелец!')
            elif mes=='декабрь':
                if chiss<22:
                    print('Ваш знак зодиака - стрелец!')
                elif chiss>21:
                    print('Ваш знак зодиака - козерог!')
            else:
                print('Укажите корректный месяц без пробелов! (Январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, октябрь, ноябрь, декабрь)')    
        else:
            print(f'Введите корректное число, в месяце нет {chiss} дней!')
    except ValueError:
        print('Укажите корректное число! (От 1 до 31(29) включительно)')
