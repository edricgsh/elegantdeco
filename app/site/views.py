# elegantdeco/app/site/views.py
from flask import abort, render_template
from app.models import Category, Product
from app.site import site
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


# Index page
@site.route('/')
def index():
    parent_categories = Category.query.filter_by(category_id=None).all()
    inventories = dict()
    db_url = os.environ.get('SQLALCHEMY_DATABASE_URI')
    db_engine = create_engine(db_url)
    Session = sessionmaker(bind=db_engine)
    session = Session()
    for category in parent_categories:
        print(category.name)
        total_products = session.query(Category, Product). \
            filter(Category.id == Product.category_id). \
            filter(Category.category_id == category.id).all()
        sum = len(total_products)
        inventories[category] = sum
    return render_template('site/index.html', inventories=inventories, title="Welcome")


@site.route('/terms')
def terms():
    return render_template('site/terms.html', title="Terms")


@site.route('/returns')
def returns():
    return render_template('site/returns.html', title="Returns")


@site.route('/shipping')
def shipping():
    return render_template('site/shipping.html', title="Shipping")


# Categories page
@site.route('/categories/<int:id>', methods=['GET', 'POST'])
def categories(id):
    categories = Category.query.filter_by(category_id=id)
    db_url = os.environ.get('SQLALCHEMY_DATABASE_URI')
    db_engine = create_engine(db_url)
    Session = sessionmaker(bind=db_engine)
    session = Session()
    total_products = session.query(Category, Product). \
        filter(Category.id == Product.category_id). \
        filter(Category.category_id == id).all()
    sum = len(total_products)
    return render_template('site/categories.html', parent_num=sum,
                           categories=categories, title="Κατηγορία")

    # Products page
    @site.route('/products/<int:id>', methods=['GET', 'POST'])
    def products(id):
        products = Product.query.filter_by(category_id=id)
        return render_template('site/products.html', products=products, title="products")

    # Product page
    @site.route('/product/<int:id>', methods=['GET', 'POST'])
    def product(id):
        products = Product.query.filter_by(id=id)
        return render_template('site/product.html', products=products, title=products)
