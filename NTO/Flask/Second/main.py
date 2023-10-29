from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Staff %r>' % self.id

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Staff %r>' % self.id

# user block


@app.route('/')
def index():
    return render_template('user/index.html', tit='Главная страница')


@app.route('/about/')
def about():
    staff = Staff.query.order_by(Staff.date.desc()).all()
    return render_template('user/about.html', tit='Про нас', staff=staff)


@app.route('/products/')
def prod():
    products = Product.query.order_by(Product.date.desc()).all()
    return render_template('user/products.html', tit='Продукты', products=products)


@app.route('/staff/<int:id>')
def more_staff(id):
    staff = Staff.query.get(id)
    return render_template('user/more_staff.html', staff=staff, tit='Детальнее')


# admin block


@app.route('/6VKBw7X$ThNcFy&', methods=['POST', 'GET'])
def index_a():
    if request.method == 'POST':
        if request.form['val'] == 'staff':
            return redirect('/create_staff')
        else:
            return redirect('/create_prod')
    else:
        return render_template('admin/index_a.html', tit='Главная страница')


@app.route('/product/<int:id>')
def more_product(id):
    product = Product.query.get(id)
    return render_template('user/more_product.html', product=product, tit='Детальнее')


@app.route('/create_staff', methods=['POST', 'GET'] )
def create():
    if request.method == 'POST':
        name = request.form['name']
        last = request.form['last']
        text = request.form['text']
        person = Staff(name=name, last=last, text=text)
        try:
            db.session.add(person)
            db.session.commit()
            return redirect('/about/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/error.html', tit='Ошибка')
    else:
        return render_template('admin/create_staff.html', tit='Добавить')


@app.route('/create_prod', methods=['POST', 'GET'])
def create_prod():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        product = Product(title=title, intro=intro, text=text)
        try:
            db.session.add(product)
            db.session.commit()
            return redirect('/products/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/error.html', tit='Ошибка')
    else:
        return render_template('admin/create_prod.html', tit='Добавить')
    

@app.route('/products/6VKBw7X$ThNcFy&')
def products_ad():
    products = Product.query.order_by(Product.date.desc()).all()
    return render_template('admin/products_ad.html', products=products, tit='Продукты')


@app.route('/about/6VKBw7X$ThNcFy&')
def staff_ad():
    staff = Staff.query.order_by(Staff.date.desc()).all()
    return render_template('admin/staff_ad.html', staff=staff, tit='Персонал')


@app.route('/product/6VKBw7X$ThNcFy&/<int:id>')
def more_product_ad(id):
    product = Product.query.get(id)
    return render_template('admin/more_product_ad.html', product=product, tit='Детальнее')


@app.route('/about/6VKBw7X$ThNcFy&/<int:id>')
def more_staff_ad(id):
    staff = Staff.query.get(id)
    return render_template('admin/more_staff_ad.html', staff=staff, tit='Детальнее')


@app.route('/about/del/<int:id>')
def delete(id):
    staff = Staff.query.get_or_404(id)
    try:
        db.session.delete(staff)
        db.session.commit()
        return redirect('/about/6VKBw7X$ThNcFy&')
    except:
        return render_template('admin/error.html', tit='Ошибка')
    
@app.route('/products/del/<int:id>')
def delete_prod(id):
    product = Product.query.get_or_404(id)
    try:
        db.session.delete(product)
        db.session.commit()
        return redirect('/products/6VKBw7X$ThNcFy&')
    except:
        return render_template('admin/error.html', tit='Ошибка')


@app.route('/products/upd/<int:id>', methods=['POST', 'GET'])
def update(id):
    product = Product.query.get(id)
    if request.method == 'POST':
        product.title = request.form['title']
        product.intro = request.form['intro']
        product.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/products/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/error.html', tit='Ошибка')
    else:
        return render_template('admin/update_prod.html', tit='Редактирование', product=product)


@app.route('/about/upd/<int:id>', methods=['POST', 'GET'])
def update_staff(id):
    staff = Staff.query.get(id)
    if request.method == 'POST':
        staff.name = request.form['name']
        staff.last = request.form['last']
        staff.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/about/6VKBw7X$ThNcFy&')
        except:
            return render_template('admin/error.html', tit='Ошибка')
    else:
        return render_template('admin/update_staff.html', tit='Редактирование', staff=staff)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)