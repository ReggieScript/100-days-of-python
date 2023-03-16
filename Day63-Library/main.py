from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy, session, query

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

with app.app_context():
    db.create_all()

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books = all_books)
    

@app.route("/add", methods= ["GET","POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")
        new_book = Book(title= title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
    return render_template("add.html")

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    if request.method == "POST":
        rating = request.form.get("new_rating")
        bookid= request.form["id"]
        book = Book.query.get(bookid)
        book.rating = rating
        db.session.commit()
        return app.redirect("/")
    bookid = request.args.get('id')
    book = Book.query.get(bookid)
    return render_template("edit.html", book = book)

if __name__ == "__main__":
    app.run(debug=True)

