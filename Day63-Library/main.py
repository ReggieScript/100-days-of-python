from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy, session

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

app.app_context().push()
db.create_all()

# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

all_books = session.query(Book).all()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/')
def home():
    return render_template("index.html", books = all_books)
    

@app.route("/add", methods= ["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = Book(title= title, author=author, rating=rating)
        db.session.add(new_book)
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

