# app/admin/views.py
from flask import abort, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_required
from app.admin import admin
from app.admin.forms import DepartmentForm, EmployeeAssignForm, RoleForm, CategoryForm, ProductForm
from .. import db
from app.models import Department, Employee, Role, Category, Product
#Prevent non-admins from accessing the page
def check_admin():
    if not current_user.is_admin:
        abort(403)

# Dashboard page
@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html', title="Dashboard")
# add admin dashboard view
@admin.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)
    return render_template('admin/admin_dashboard.html', title="Dashboard")

#--Department Views--
#List Departments
@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    check_admin()
    departments = Department.query.all()
    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")
#Add a department
@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    check_admin()
    add_department = True
    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')
        # redirect to departments page
        return redirect(url_for('admin.list_departments'))
    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")
#Edit a department
@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    check_admin()
    add_department = False
    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')
        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))
    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")
#Delete a department
@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    check_admin()
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')
    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))
    return render_template(title="Delete Department")
#--Role Views--
#List roles
@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')
#Add a role
@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    check_admin()
    add_role = True
    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)
        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')
        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))
    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')
#Edit a role
@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    check_admin()
    add_role = False
    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')
        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))
    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")
#Delete a role
@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    check_admin()
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')
    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))
    return render_template(title="Delete Role")
#--Employee Views--
#List Employees
@admin.route('/employees')
@login_required
def list_employees():
    check_admin()
    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')
#Assign a department and a role to an employee
@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    check_admin()
    employee = Employee.query.get_or_404(id)
    # prevent admin from being assigned a department or role
    if employee.is_admin:
        abort(403)
    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')
        # redirect to the employees page
        return redirect(url_for('admin.list_employees'))
    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')
# Category Views
#List Categories
@admin.route('/categories', methods=['GET', 'POST'])
@login_required
def list_categories():
    check_admin()
    categories = Category.query.all()
    return render_template('admin/categories/categories.html',
                           categories=categories, title="Category")
#--Add Category--
@admin.route('/categories/add', methods=['GET', 'POST'])
@login_required
def add_category():
    check_admin()
    categories = Category.query.all()
    add_category = True
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data,
                                description=form.description.data, category_id=form.category_id.data)
        try:
            # add category to the database
            db.session.add(category)
            db.session.commit()
            flash('You have successfully added a new category.')
        except:
            # in case category name already exists
            flash('Error: category name already exists.')
        # redirect to category page
        return redirect(url_for('admin.list_categories'))
    # load category template
    return render_template('admin/categories/category.html', action="Add",
                           add_category=add_category, form=form,
                           title="Add Categories", categories=categories)
#Edit Category
@admin.route('/categories/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    check_admin()
    categories = Category.query.all()
    add_category = False
    category = Category.query.get_or_404(id)
    form = CategoryForm(obj=category)
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.category_id = form.category_id.data
        db.session.commit()
        flash('You have successfully edited the category.')
        # redirect to the categories page
        return redirect(url_for('admin.list_categories'))
    form.description.data = category.description
    form.name.data = category.name
    form.category_id.data = category.id
    return render_template('admin/categories/category.html', action="Edit",
                           add_category=add_category, form=form,
                           categories=categories, title="Edit Category")
#Delete Category
@admin.route('/categories/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_category(id):
    check_admin()
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('You have successfully deleted the category.')
    # redirect to the categories page
    return redirect(url_for('admin.list_categories'))
    return render_template(title="Delete Category")
#--Product Views--
#List Products
@admin.route('/products', methods=['GET'])
@login_required
def list_products():
    check_admin()
    products = Product.query.all()
    return render_template('admin/products/products.html',
                               products=products, title="Products")
#Add a product
@admin.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    check_admin()
    add_product = True
    form = ProductForm(request.form)
    if form.validate_on_submit():
        product = Product(code=form.code.data,
                                    name=form.name.data, price=form.price.data, category=form.category.data)
        
        try:
            db.session.add(product)
            db.session.commit()
            flash('You have successfully added a new product.')
        except:
            # in case product name already exists
            flash('Error: product name already exists.')
        # redirect to departments page
        return redirect(url_for('admin.list_products'))
    # load product template
    return render_template('admin/products/product.html', action="Add",
                           add_product=add_product, form=form,
                           title="Add Product")
#Delete Product
@admin.route('/products/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_product(id):
    check_admin()
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('You have successfully deleted the product.')
    # redirect to the products page
    return redirect(url_for('admin.list_products'))
    return render_template(title="Delete Product")
#Edit a product
@admin.route('/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_product(id):
        check_admin()
        add_product = False
        product = Product.query.get_or_404(id)
        form = ProductForm(obj=product)
        if form.validate_on_submit():
            product.code = form.code.data
            product.name = form.name.data
            product.price = form.price.data
            product.category= form.category.data
            db.session.commit()
            flash('You have successfully edited the products.')
            return redirect(url_for('admin.list_products'))
        form.code.data = product.code
        form.name.data = product.name
        form.price.data = product.price
        form.category.data= product.category
        return render_template('admin/products/product.html', action="Edit",
                           add_product=add_product, form=form,
                           product=product, title="Edit Product")