from flask import Flask
from flask import render_template
import random

random_number=random.randint(0,9)

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)