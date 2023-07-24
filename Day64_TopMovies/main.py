from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
import credentials
import requests

# Define variables

app = Flask(__name__)
app.config['SECRET_KEY'] = credentials.SECRET_KEY
Bootstrap(app)
TMDB_API_KEY = credentials.TMDB_API_KEY

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)


# Define the form
class RateMovieForm(FlaskForm):
    rating = IntegerField(label = "Your rating out of 10 eg. 7.5")
    review = StringField(label = "Your review")
    submit = SubmitField(label="Done")

# Define the SQL table

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=True, nullable=True)
    review = db.Column(db.String, unique=False, nullable=True)
    img_url = db.Column(db.String, unique=False, nullable=False)


    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

# Adding a movie


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    rank = len(all_movies)
    for movie in all_movies:
        movie.ranking = rank
        rank -=1
        print(movie.ranking)

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
        print(movie_data)
        movie_data = eval(movie_data)
        new_movie = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"].split("-")[0],
        description=movie_data["overview"],
        img_url="https://www.themoviedb.org/t/p/original" + movie_data["poster_path"]
        )
    

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id = new_movie.id))

@app.route("/edit", methods = ["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit:
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        with app.app_context():
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie = movie, form = form)

if __name__ == '__main__':

    app.run(debug=True)
