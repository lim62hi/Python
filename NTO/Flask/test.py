from flask import Flask

app = Flask(__name__)

@app.route('/home/')
@app.route('/')
def home():
    return 'You\'re at home!'

@app.route('/about/')
def about():
    return 'In this part of site have written about us!'

if __name__ == '__main__':
    app.run(debug=True)