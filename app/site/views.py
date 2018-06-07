# elegantdeco/app/site/views.py
from flask import abort, render_template
from app.models import Category, Product
from app.site import site
# Index page
@site.route('/')
def index():
    return render_template('site/index.html', title="Welcome")
@site.route('/terms')
def terms():
    return render_template('site/terms.html', title="Terms")
@site.route('/returns')
def returns():
    return render_template('site/returns.html', title="Returns")
@site.route('/shipping')
def shipping():
    return render_template('site/shipping.html', title="Shipping")
