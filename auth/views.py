# -*- coding:utf-8 -*-
from flask import render_template, redirect, request, url_for, flash,g
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import RegistrationForm,ChangePasswordForm,LoginForm
from modles import User,db



@auth.route('/login',methods=('GET', 'POST'))
def login():
    # if g.user is not None and g.user.is_authenticated():
    #     return redirect(url_for('user.index'))
    form = LoginForm()

    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            g.username = form.username.data
            login_user(user)
            if g.username == 'admin':
                return redirect(request.args.get('next') or url_for('admin.index'))
            return redirect(request.args.get('next') or url_for('user.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

@auth.route('/register',methods=('GET','POST'))
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data
        if User.query.filter_by(username=username).first() is not None:
            print(1)
            flash('用户名已被占用')
            return redirect(url_for('auth.register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form = form)


@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if request.method == 'POST':
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            logout_user()
            return redirect(url_for('auth.login'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html",form = form)
