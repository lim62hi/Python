import requests
import json

genres = requests.get('https://yupest2.pythonanywhere.com/api/v1.0/books/genres').json()['records']
books = []

for genre in genres:
    r = requests.get(f'https://yupest2.pythonanywhere.com/api/v1.0/books/?genre={genre}').json()['records']
    print(r[0]['Название'])
    books.append(r)

print(f'Количество записей: {len(books)}')

with open('books.json', 'w') as f:
    json.dump(books, f)