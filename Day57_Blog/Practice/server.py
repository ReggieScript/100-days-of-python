from flask import Flask
from flask import render_template
import random
import datetime

random_number=random.randint(0,9)

app = Flask(__name__)


@app.route("/")
def main_page():
    num_year = datetime.date.today().year
    return render_template("index.html", real_year=num_year)


if __name__ ==  "__main__": ## Checks if this file is the main file.    
    app.run(debug=True)