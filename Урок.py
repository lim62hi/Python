d=input('Когда вы хотите сделать задачу? ')
z=input('Какую задачу вы хотите сделать? ')
d1=input('Когда вы хотите сделать задачу? ')
z1=input('Какую задачу вы хотите сделать? ')
d2=input('Когда вы хотите сделать задачу? ')
z2=input('Какую задачу вы хотите сделать? ')
spi={d: z, d1: z1, d2: z2}
znach=input('На какой день вы хотите посмотреть задачу? ')
g=spi[znach]
print(f'Вы должны {znach} {g}!')
