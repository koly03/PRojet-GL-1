from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField, DateField
from wtforms.validators import DataRequired, Length,Email
import email_validator
from wtforms.fields.html5 import TimeField




class ContactForm(FlaskForm):
    name = StringField('NAME',validators=[DataRequired('A full name is required'), Length(min=5,max=30)])
    email = StringField('EMAIL',validators=[DataRequired('A correct email is required'), Email()])
    message = StringField('MESSAGE', validators=[DataRequired('A message is required'), Length(min=5,max=500)])
    date = DateField('DATE', format='%Y-%m-%d', validators=[DataRequired('Please enter a date')])
    time = TimeField('TIME', validators=[DataRequired('Please enter a time')])
    submit = SubmitField('SEND')


