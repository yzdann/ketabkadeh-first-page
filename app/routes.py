# -*- coding: utf-8 -*-
from flask import render_template, flash
from app import app, db, limiter
from app.forms import NotifyMeForm
from app.models import User


@app.route('/', methods=['GET', 'POST'])
@limiter.limit("40 per day")
def index():
    form = NotifyMeForm()
    if form.validate_on_submit():
        user = User.query.filter(
                User.telegram_id.ilike(form.telegram_id.data)
        ).first()
        if user is not None:
            flash('این نام کاربری که میزنی قبلاً ثبت شده که')
        else:
            user = User(telegram_id=form.telegram_id.data)
            db.session.add(user)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html', form=form)
