from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, NumberRange

app = Flask(__name__)

all_books = []

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Missing functionality of the empty library paragraph.

@app.route('/')
def home():
    send_books = []
    books = all_books
    for book in books:
        item = book["title"] + ' - ' + book["author"] + ' - ' + book["rating"] + "/10"
        send_books.append(item)
    return render_template("index.html", books = send_books)
    

@app.route("/add", methods= ["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        book = {
            "title": title,
            "author": author,
            "rating": rating,
        }
        all_books.append(book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

