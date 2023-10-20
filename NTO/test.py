import requests

genres = ['зарубежное', 'приключения']
books = []
count = 0
for genre in genres:
    b = []
    res = requests.get(f'https://yupest2.pythonanywhere.com/api/v1.0/books/?age=7&genre={genre}').json()['records']
    l = len(res)
    i = 0
    while i < l:
        b.append(res[i]['code'])
        i += 1
    books.append(b)
print(books)
for i in books[0]:
    if i in books[1]: 
        count +=1
print(count)