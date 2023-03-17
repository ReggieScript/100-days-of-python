from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, URL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class RateMovieForm(FlaskForm):
    rating = IntegerField(label = "Your rating out of 10 eg. 7.5")
    review = StringField(label = "Your review")
    submit = SubmitField(label="Done")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=True, nullable=False)
    review = db.Column(db.String, unique=False, nullable=False)
    img_url = db.Column(db.String, unique=False, nullable=False)


    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()



# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )

# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies = all_movies)

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    form = RateMovieForm(request.form)
    movieid = request.args.get('id')
    if request.method == "POST":
        movie = Movie.query.get(movieid)
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return app.redirect('/')
    movie = Movie.query.get(movieid)
    return render_template("edit.html",movie = movie, form = form)

@app.route("/delete")
def delete():
    movieid = request.args.get('id')
    movie = Movie.query.get(movieid)
    db.session.delete(movie)
    db.session.commit()
    return app.redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
