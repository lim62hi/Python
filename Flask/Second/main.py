from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    last = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Staff %r>' % self.id

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cast = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20), nullable=False)
    place = db.Column(db.String(20), nullable=False)
    HELP = db.Column(db.String(30), nullable=False)
    button = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Staff %r>' % self.id

def head(request):
    if request.form['val'] == 'staff':
        return redirect('/create_staff')
    else:
        return redirect('/create_prod')


# user block
# main page

@app.route('/')
def index():
    return render_template('user/index.html', tit='Главная страница')

# info

@app.route('/stafs/')
def staff():
    stafs = Staff.query.order_by(Staff.date.desc()).all()
    return render_template('user/info/stafs.html', tit='Про нас', stafs=stafs)


@app.route('/prods/')
def prod():
    prods = Product.query.order_by(Product.date.desc()).all()
    return render_template('user/info/prods.html', tit='Продукты', prods=prods)

# more

@app.route('/stafs/<int:id>')
def more_staff(id):
    stafs = Staff.query.get(id)
    return render_template('user/more/more_stafs.html', stafs=stafs, tit='Детальнее')


@app.route('/prods/<int:id>', methods=['GET', 'POST'])
def more_prod(id):
    prods = Product.query.get(id)
    return render_template('user/more/more_prods.html', prods=prods, tit='Детальнее')

# buy

@app.route('/buy/<int:cast>')
def buy(cast):
    return render_template('user/other/cast.html', tit='Оплата', cast=cast)

# admin block
# main page

@app.route('/6VKBw7X$ThNcFy&', methods=['POST', 'GET'])
def index_a():
    if request.method == 'POST':
        return head(request)
    else:
        return render_template('admin/index_a.html', tit='Главная страница')

# info for admins    

@app.route('/prods/6VKBw7X$ThNcFy&', methods=['POST', 'GET'])
def prod_ad():
    if request.method == 'POST':
        return head(request)
    else:
        prods = Product.query.order_by(Product.date.desc()).all()
        return render_template('admin/info/prods_ad.html', prods=prods, tit='Продукты')


@app.route('/stafs/6VKBw7X$ThNcFy&', methods=['POST', 'GET'])
def staff_ad():
    if request.method == 'POST':
        return head(request)
    else:
        staff = Staff.query.order_by(Staff.date.desc()).all()
        return render_template('admin/info/stafs_ad.html', staff=staff, tit='Персонал')

# more for admins

@app.route('/prods/6VKBw7X$ThNcFy&/<int:id>', methods=['POST', 'GET'])
def more_product_ad(id):
    if request.method == 'POST':
        return head(request)
    else:
        product = Product.query.get(id)
        return render_template('admin/more/more_prods_ad.html', product=product, tit='Детальнее')


@app.route('/stafs/6VKBw7X$ThNcFy&/<int:id>', methods=['POST', 'GET'])
def more_staff_ad(id):
    if request.method == 'POST':
        return head(request)
    else:
        staff = Staff.query.get(id)
        return render_template('admin/more/more_stafs_ad.html', staff=staff, tit='Детальнее')

# create

@app.route('/create_staff', methods=['POST', 'GET'])
def create_staff():
    if request.method == 'POST':
        name = request.form['name']
        last = request.form['last']
        text = request.form['text']
        age = request.form['age']
        person = Staff(name=name, last=last, text=text, age=age)
        try:
            db.session.add(person)
            db.session.commit()
            return redirect('/stafs/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/other/error.html', tit='Ошибка')
    else:
        return render_template('admin/create/create_stafs.html', tit='Добавить')


@app.route('/create_prod', methods=['POST', 'GET'])
def create_prod():
    if request.method == 'POST':
        title = request.form['title']
        cast = request.form['cast']
        place = request.form['place']
        HELP = request.form['HELP']
        button = request.form['button']
        text = request.form['text']
        product = Product(text=text, title=title, cast=cast, place=place, HELP=HELP, button=button)
        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/prods/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/other/error.html', tit='Ошибка')
    else:
        return render_template('admin/create/create_prods.html', tit='Добавить')

# deleting

@app.route('/stafs/del/<int:id>')
def delete_staff(id):
    staff = Staff.query.get_or_404(id)
    try:
        db.session.delete(staff)
        db.session.commit()
        return redirect('/stafs/6VKBw7X$ThNcFy&')
    except:
        return render_template('admin/other/error.html', tit='Ошибка')
    

@app.route('/prods/del/<int:id>')
def delete_prod(id):
    product = Product.query.get_or_404(id)
    try:
        db.session.delete(product)
        db.session.commit()
        return redirect('/prods/6VKBw7X$ThNcFy&')
    except:
        return render_template('admin/other/error.html', tit='Ошибка')

# updating

@app.route('/prods/upd/<int:id>', methods=['POST', 'GET'])
def update_prod(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.cast = request.form['cast']
        product.place = request.form['place']
        product.HELP = request.form['HELP']
        product.button = request.form['button']
        product.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/prods/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/other/error.html', tit='Ошибка')
    else:
        return render_template('admin/update/update_prods.html', tit='Редактирование', product=product)


@app.route('/stafs/upd/<int:id>', methods=['POST', 'GET'])
def update_staff(id):
    staff = Staff.query.get(id)
    if request.method == 'POST':
        staff.name = request.form['name']
        staff.last = request.form['last']
        staff.text = request.form['text']
        staff.age = request.form['age']
        try:
            db.session.commit()
            return redirect('/stafs/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/other/error.html', tit='Ошибка')
    else:
        return render_template('admin/update/update_stafs.html', tit='Редактирование', staff=staff)

# buy

@app.route('/buy/6VKBw7X$ThNcFy&/<int:cast>', methods=['POST', 'GET'])
def buy_ad(cast):
    if request.method == 'POST':
        return head(request)
    else:
        return render_template('admin/other/cast_ad.html', tit='Оплата', cast=cast)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)