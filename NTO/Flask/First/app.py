from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
@app.route('/home/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(title=title, intro=intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/articles')
        except:
            return 'Error'
    else:
        return render_template('create.html')

@app.route('/articles/')
def articles():
    art = Article.query.order_by(Article.date.desc()).all()
    return  render_template('articles.html', articles=art)


@app.route('/articles/<int:id>')
def more(id):
    art = Article.query.get(id)
    return render_template('more.html', article=art)

@app.route('/articles/del/<int:id>')
def delete(id):
    art = Article.query.get_or_404(id)
    try:
        db.session.delete(art)
        db.session.commit()
        return redirect('/articles')
    except:
        return 'Error for deleting of article'
    

@app.route('/articles/upd/<int:id>', methods=['POST', 'GET'])
def update(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/articles')
        except:
            return 'Error'
    else:
        return render_template('upd.html', article=article)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)