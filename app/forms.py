# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class NotifyMeForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
