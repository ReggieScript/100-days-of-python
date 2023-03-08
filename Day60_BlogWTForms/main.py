from flask import Flask
from flask import render_template, request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextAreaField
import requests
import smtplib
import os
import email
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

send_email = os.getenv("MAIL_SEND") 
recieve_email = os.getenv("MAIL_RECIEVE")
password_email = os.getenv("PASSWORD")

blogs_url = "https://api.npoint.io/54484abb664011e3248c"

# form = FlaskForm()

@app.route("/")
def home():
    return render_template("index.html")

class SignupForm(FlaskForm(meta={'csrf': False})):
    username = TextAreaField('Username')
    recaptcha = RecaptchaField()

@app.route("/login")
def login():
    form = SignupForm()
    return render_template("login.html", form)

if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)