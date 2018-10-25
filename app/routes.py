# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import NotifyMeForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NotifyMeForm()
    if form.validate_on_submit():
        # check for duplicated email
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('این ایمیلی که میزنی قبلاً ثبت شده که')
        # create user
        else:
            user = User(email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('رواله :) خبرت می‌کنیم')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)