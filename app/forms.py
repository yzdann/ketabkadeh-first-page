# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class NotifyMeForm(FlaskForm):
    telegram_id = StringField(validators=[
            DataRequired(),
            Length(4, 50, 'نام کاربری باید حداقل شامل پنج کاراکتر باشد'),
    ])
    recaptcha = RecaptchaField()
