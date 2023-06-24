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
TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzNzViYWMzYTZjZGQ0ODBjMmNmZTMwMWQwNWM1OWIzOCIsInN1YiI6IjY0OTVmOTkwYTE0YmVmMDBhZDJjMTBmNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pBlvs6p6XSo3iNcovE2J32xQAwLDVCfw_U0QMTuvsls"

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

# Code to add a movie
def add_movie(movie_data):
    new_movie = Movie(
        title=movie_data.title,
        year=movie_data.release_date.split("-")[0],
        description=movie_data.overview,
        rating=7.3,
        ranking=10,
        review="",
        img_url=movie_data.poster_path
    )
    
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies = all_movies)

@app.route("/edit", methods = ["GET","POST"])
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

class AddMovieForm(FlaskForm):
    title = StringField(label = "Movie Title")
    submit = SubmitField(label="Add Movie")


@app.route("/add", methods = ["GET","POST"])
def add():
    form = AddMovieForm(request.form)
    if form.validate_on_submit():
        movie_title = form.title.data
        tmdb_url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
        tmdb_headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}" }
        response = requests.get(tmdb_url, headers = tmdb_headers)
        data = response.json()["results"]
        return render_template("select.html", movies = data)

    return render_template("add.html", form = form)

@app.route("/find")
def find_movie():
    movie_data = request.args.get("data")
    if movie_data:
        add_movie(movie_data)
        return redirect(url_for("home"))

if __name__ == '__main__':

    app.run(debug=True)
