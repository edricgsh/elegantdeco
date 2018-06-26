# elegantdeco/app/site/views.py
from flask import abort, render_template
from app.models import Category, Product
from app.site import site


# Index page
@site.route('/')
def index():
    products = Product.query.filter_by(category_id=1)
    print(products)
    return render_template('site/index.html', products=products, title="Welcome")


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
    sum = 0
    # In categories, there are all the sub categories
    for category in categories:
        # For each sub category, do a query to get all the product size
        # and add all of them together
        products = Product.query.filter_by(category_id=category.id).all()
        sum += len(products)

    # Pass the parent category sum of products to the html page
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
