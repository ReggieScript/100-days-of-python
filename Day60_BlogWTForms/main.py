from flask import Flask
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import os
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

load_dotenv()

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def home():
    return render_template("index.html")

class SignupForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField(label ="Password", validators=[DataRequired(), Length(min = 8)])
    submit = SubmitField(label="Log In")

# SignupForm(meta={'csrf': False})

@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignupForm(request.form)
    print(request.method)
    form.validate_on_submit()
    if request.method == "POST" and form.validate_on_submit():
        print(form.username.data)
        if form.username.data == "admin@email.com" and form.password.data == "12345678":
            return app.redirect("/success")
        else:
            return app.redirect("/denied")
    return render_template("login.html", form = form)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/denied")
def denied():
    return render_template("denied.html")

if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)