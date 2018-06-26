# app/admin/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Department, Role, Employee, Category, Product

class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(), get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(), get_label="name")
    submit = SubmitField('Submit')

class CategoryForm(FlaskForm):
    """
    Form for admin to add or edit a category
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    category_id = StringField('Category_id', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ProductForm(FlaskForm):
    """
    Form for admin to add or edit a product
    """
    code = StringField('Code', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    category = QuerySelectField(query_factory=lambda: Category.query.all(), get_label="name")
    """description = StringField('Description', validators=[DataRequired()])"""
    price = IntegerField('Price', validators=[DataRequired()])


    submit = SubmitField('Submit')


