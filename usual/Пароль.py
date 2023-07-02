print('Регистрация')
login=input('Введите ваш логин: ')
parol=input('Введите пароль: ')
print('Поздравляем, вы зарегестрированы! Теперь войдите в свой аккаунт')
print('Вход')
num= -3
while num!=0:
    num+=1
    if num== -2:
        print('У вас есть три попытки!')
    login1=input('Логин: ')
    parol1=input('Пароль: ')
    if login1 == login and parol1 == parol:
        print('Вы успешно вошли в свой аккаунт!')
        break
    else:
        print('Неправильный логин или пароль!')
