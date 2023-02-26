from flask import Flask
from flask import render_template
import random
import requests
import json

random_number=random.randint(0,9)

app = Flask(__name__)


@app.route("/guess/<name>")
def prediction(name):
    gender_request = requests.get(url = f"https://api.genderize.io?name={name}").json()["gender"]
    age_request = requests.get(url = f"https://api.agify.io?name={name}").json()["age"]
    return render_template("index_predict.html",user_name= name, gender = gender_request, age = age_request)


@app.route("/")
def main_page():
    return render_template("index.html")


if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)