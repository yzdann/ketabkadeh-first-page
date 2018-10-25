# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class NotifyMeForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()
