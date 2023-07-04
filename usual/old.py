while True: 
    try:
        ago = int(input('В каком году вы родились? '))
        now = int(input('Какой сейчас год? '))
        old = now - ago
        print(f'Скорее всего вам сейчас {old} лет!')
    except:
        print('Введите корректные даты!')