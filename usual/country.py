while True:
    item = { 
        'russia': {
        'name': 'Russia',
        'code': 'RU', 
        'population': 144
        },
        'usa': {
            'name': 'Unated States of America',
            'code': 'USA',
            'population': 250
        }
    }
    try:
        country = input('country: ').lower()
        x = input('name, code or the population: ').lower()
        print(item[country][x])
    except:
        print('irregular search!')