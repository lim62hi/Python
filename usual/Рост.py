while True:
    spot=int(input('Рост первого спортсмена: '))
    spot1=int(input('Рост второго спортсмена: '))
    spot2=int(input('Рост третьего спортсмена: '))
    if spot<spot1<spot2:
        print('Они стоят по росту!')
    elif spot>spot1>spot2:
        print('Они стоят по росту!')
    else:
        print('Они стоят не по росту!')
