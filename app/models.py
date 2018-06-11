# elegantdeco/app/models.py
from app import db

Product_categories = db.Table('product_categories',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('products.id', ondelete="cascade")),
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id', ondelete="cascade")))


# Category table
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(50))
    categoty_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    def __repr__(self):
        return '<Category: {}>'.format(self.name)

# Product table
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(5000), index=True)
    image = db.Column(db.String(50))
    category = db.relationship('Category', secondary=Product_categories, backref=db.backref('products'))
    def __repr__(self):
        return '<Product: {}>'.format(self.name)
