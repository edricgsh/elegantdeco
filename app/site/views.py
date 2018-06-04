# app/site/views.py
from flask import abort, render_template
from app.site import site
# Index page
@site.route('/')
def index():
    return render_template('site/index.html', title="Welcome")
