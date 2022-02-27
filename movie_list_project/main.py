from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

API_KEY = os.environ.get('MOVIE_API_KEY')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(240), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(100), nullable=True)
    img_url = db.Column(db.String)


db.create_all()


class RateForm(FlaskForm):
    rating = StringField('Rating Out of 10 - (7.5)',
                         validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    title = StringField('Movie Title')
    submit = SubmitField('Add Movie')


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route('/edit', methods=["POST", "GET"])
def rate_movie():
    form = RateForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    print(f"===>>> movie {movie} and ID {movie_id}")
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=movie)


@app.route('/delete', methods=["POST", "GET"])
def delete():
    movie_id = request.args.get('id')
    delete_movie = Movie.query.get(movie_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=["POST", "GET"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                params={'api_key': API_KEY, 'query': movie_title})
        data = response.json()['results']
        return render_template('select.html', data=data)
    return render_template('add.html', form=form)


@app.route('/find')
def find():
    movie_api_id = request.args.get('id')
    print(f"movie ID in FIND is ==>>>> [{movie_api_id}")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response = requests.get(movie_api_url, params={
                                'api_key': API_KEY, 'language': 'en-US'})
        data = response.json()
        new_movie = Movie(
            title=data['title'],
            year=data['release_date'].split("-")[0],
            description=data['overview'],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
