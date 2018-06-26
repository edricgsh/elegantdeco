# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app.auth import auth
from app.auth.forms import LoginForm
from .. import db
from app.models import Employee


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)

            # redirect to the appropriate dashboard page
            if employee.is_admin:
                return redirect(url_for('admin.admin_dashboard'))
            else:
                return redirect(url_for('admin.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
