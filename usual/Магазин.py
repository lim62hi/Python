price=dict(мясо = 500, хлеб= 42, воду = 82)
def buy ():
    pay = 0 
    print('Вода стоит 82 рубля, хлеб стоит 42 рубля, мясо стоит 500 рублей.')
    while True:
        x=input('Что хотите купить? Чтобы завершить покупку введите "завершить" ')
        if x == 'завершить':
            break
        pay +=price[x]
    return pay
print('К оплате', buy(), 'руб.')
print('Спасибо за покупку!')
