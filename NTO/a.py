from flask import Flask, request, jsonify, make_response
import requests
from random import choice

app = Flask(__name__)
   # настройка поддержки кириллицы
app.config['JSON_AS_ASCII'] = True

   # маршрут по умолчанию
@app.route('/')
def index():
   return 'Hello from Flask!'

def get_book(author):
     # список книг по автору
  books = requests.get(f'https://yupest2.pythonanywhere.com/api/v1.0/books/?author={author}').json()['records']

     # случайная книга в диапазоне от нулевого до последнего из списка
  book = choice(books)

     # строка ответа бота с рекомендацией книги
  return f'''{book['Название']}
      Автор: {book['Автор']}
      Оценка: {book['Оценка']}
      Код книги: {book['code']}'''

def get_result():
      # извлечение параметра
   req = request.get_json(force=True)
   author = req['queryResult']['parameters']['authors']

      # если параметр задан, вернем случайный фильм
   if author:
       return {'fulfillment': get_book(author)}

   # маршрут webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
   return make_response(jsonify(get_result()))

app.run(host='0.0.0.0', port=5000)