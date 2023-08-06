from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(4))
    rated = db.Column(db.String(10))
    released = db.Column(db.String(20))
    runtime = db.Column(db.String(20))
    genre = db.Column(db.String(120))
    director = db.Column(db.String(120))
    writer = db.Column(db.String(120))
    actors = db.Column(db.String(255))
    plot = db.Column(db.Text)
    language = db.Column(db.String(50))
    country = db.Column(db.String(50))
    awards = db.Column(db.Text)
    poster = db.Column(db.String(255))
    imdb_rating = db.Column(db.String(5))
    metascore = db.Column(db.String(5))
    imdb_votes = db.Column(db.String(20))
    imdb_id = db.Column(db.String(20))
