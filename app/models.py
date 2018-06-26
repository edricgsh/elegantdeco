# elegantdeco/app/models.py
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager


# Category table
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(200))
    image = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    product = db.relationship('Product', backref='category', lazy='dynamic')
    def __repr__(self):
        return '<Category: {}>'.format(self.name)

# Product table
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(50), index=True, unique=True)
    description = db.Column(db.String(5000), index=True)
    price = db.Column(db.Integer)
    image = db.Column(db.String(50))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    def __repr__(self):
        return '<Product: {}>'.format(self.name)


#Employee table
class Employee(UserMixin, db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)
# Prevent password to be read
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')
# Hash password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
# Verify password
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
# Represent table
    def __repr__(self):
        return '<Employee: {}>'.format(self.username)
# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))
# Department table
class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')
    def __repr__(self):
        return '<Department: {}>'.format(self.name)
# Role table
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')
    def __repr__(self):
        return '<Role: {}>'.format(self.name)

