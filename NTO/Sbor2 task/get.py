import requests
import json

films = []
offset = 0
url = f'https://yupest2.pythonanywhere.com/api/v1.0/movies/?offset={offset}'
res = requests.get(url).json()['records']

while res!=[]:
    print(res[0]['code'])
    films.extend(res)
    offset += 30
    url = f'https://yupest2.pythonanywhere.com/api/v1.0/movies/?offset={offset}'
    res = requests.get(url).json()['records']
    
print(f'Количество записей: {len(films)}')

with open('films.json', 'w') as f:
    json.dump(films, f)