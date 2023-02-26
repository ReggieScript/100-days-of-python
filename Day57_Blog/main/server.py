from flask import Flask
from flask import render_template
import requests
import json

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/blog")
def blog_page():
    blog_data = requests.get(url = "https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", posts = blog_data)


if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)