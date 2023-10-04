import requests
import json

films = []
offset = 0
url = f'https://yupest2.pythonanywhere.com/api/v1.0/movies/?offset={offset}'
res = requests.get(url).json()['records']

while res!=[]:
    print(res[0]['code'])
    offset += 30
    url = f'https://yupest2.pythonanywhere.com/api/v1.0/movies/?offset={offset}'
    res = requests.get(url).json()['records']
    films.append(res)
    
print(f'Количество записей: {len(films)}')

with open('films.json', 'w') as f:
    json.dump(films, f)