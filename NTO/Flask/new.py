from flask import Flask

app = Flask(__name__)

@app.route('/home/')
@app.route('/')
def home():
    return 'You\'re on home page!'

@app.route('/home/users/')
def users():
    return 'You\'re on users page'

@app.route('/home/users/<id>')
def users_id(id):
    return f'You\'re on users-id page and your id is {id}'

if __name__ == '__main__':
    app.run(debug=True)