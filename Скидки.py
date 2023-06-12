price=dict(Мясо=800, Хлеб = 50, Вода = 30)
newprice={}
for i in price.keys():
    newprice[i] = round(price[i] * 0.80, 2)
for k,v in price.items():
    print(f'{k} раньше стоило {v} руб.')
print()
for k,v in newprice.items():
    print(f'{k} со скидкой в 20% стоит {v} руб.')
