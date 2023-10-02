import requests

genres = ['зарубежное', 'приключения', 'проза']
books = []
s = []
for genre in genres:
    res = requests.get(f'https://yupest2.pythonanywhere.com/api/v1.0/books/?genre={genre}').json()['records']
    l = len(res)
    i = 0
    while i < l:
        books.append(res[i]['code'])
        i += 1
    s.append(books)
    books = []
f = s[0]
t = s[2]
s = s[1]
count = 0
for i in s:
    if i in f and i in t: 
        count +=1
print(count)