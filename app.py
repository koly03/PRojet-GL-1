

# from sqlite3 import Time
from sqlalchemy import Time 
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from random import randint
from sqlalchemy.sql.sqltypes import TIME
from wtforms import TimeField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://////Users/user/Desktop/Fac/Project/Python_project/Python_project\\sqlite\\resa1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Clients(db.Model):
    __tablename__ = 'clients'
    clientid = db.Column(db.Integer, primary_key=True)
    clientname = db.Column(db.String(40), nullable=False)
    clientemail = db.Column(db.String(40), nullable=False)
    clientmessage = db.Column(db.String(200), nullable=True)
    clientdate = db.Column(db.Date, nullable=False) 
    clienttime = db.Column(Time, nullable=False) 
    def __repr__(self):
        return f"Clients('{self.clientname}', '{self.clientemail}', '{self.clientmessage}', '{self.clientdate}', '{self.clienttime}')"


with app.app_context():
    db.create_all()


class ContactForm(FlaskForm):
    name = StringField('NAME', validators=[DataRequired('A full name is required'), Length(min=5, max=30)])
    email = StringField('EMAIL', validators=[DataRequired('A correct email is required'), Email()])
    message = StringField('MESSAGE', validators=[DataRequired('A message is required'), Length(min=5, max=500)])
    date = DateField('DATE', format='%Y-%m-%d', validators=[DataRequired('Please enter a date')])
    time = TimeField('TIME', validators=[DataRequired('Please enter a time')])
    submit = SubmitField('SEND')

@app.route("/", methods=["GET", "POST"]) 
@app.route("/home", methods=["GET", "POST"]) 
def hello_world():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        date = form.date.data
        time = form.time.data
        print(name, email, message, date, time)
        db.session.add(
            Clients(
                clientid=randint(0, 1000000),
                clientname=name,
                clientemail=email,
                clientmessage=message,
                clientdate=date,
                clienttime=time
            )
        )
        db.session.commit()

        form.name.data, form.email.data, form.message.data, form.date.data, form.time.data = "", "", "", "",""
        return render_template('index.html', form=form, success=True)
    return render_template('index.html', form=form)

@app.route("/database")
def database():
    return render_template('database.html', clients=Clients.query.all())

@app.route("/Chef1", methods=["GET", "POST"])
def Chef1():
    return render_template('Chef1.html')

@app.route("/Chef2", methods=["GET", "POST"])
def Chef2():
    return render_template('Chef2.html')

@app.route("/Chef3", methods=["GET", "POST"])
def Chef3():
    return render_template('Chef3.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
