import math
pi=math.pi
try:
    def radius():
        znach=float(input('Введите диаметр циллиндра в см3: '))
        znach/=2
        return znach

    def visota():
        znach=float(input('Введите высоту циллиндра в см3: '))
        return znach

    def result():
        r=radius()
        vv=visota()
        s=pi*r**2
        v=s*vv
        return v

    v=result()

    def muss(g):
        znach=float(input('Введите удельный вес (г/см3): '))
        return g*znach/1000

    m=muss(v)
    print(f'Ответ: объем циллиндра равен {v} см3, а вес равен {m} кг!')
except:
    print('Введите корректные числа!')