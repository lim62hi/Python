country = input('Укажите страны через пробел: ').lower().split()
new_country = []
for i in country:
    if i not in new_country:
        new_country.append(i)
print(new_country)