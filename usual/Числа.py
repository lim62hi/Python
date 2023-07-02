from random import randint
a=-1
b=-1
c=-1
while a<3:
    a+=1
    c+=1
    if b==0:
        print('У вас осталось три попытки.')
    b+=1
    parol=',bpjy123'
    parol1=input('Чтобы войти введите пароль: ')
    if parol1==parol:
        print('Игра "Угадай число"')
        while True:
            try:
                x= random_number = randint(1,5)
                y = int(input('Введите число: '))
                if 0<y<6:
                    if x==y:    
                        print( f'Вы победили! Было загадано число {x}!')
                    if x!=y:
                        print(f'Вы проиграли! Было загадано число {x}!')
                if y<1 or y>5:
                    print('Пользователь, нужно ввести целое число от 1 до 5, а не какое-либо другое число!')
            except:
                print('Введите корректное число!')
    elif c==0:                 
        if parol1!=parol:
            print('Пароль введен неправильно. В доступе отказано! Попробуйте заново ввести пароль.')
