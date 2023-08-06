from flask_restful import reqparse, Resource
import requests
from app.models import Movie

class MovieSearch(Resource):
    def __init__(self, db):
        self.db = db

    def get(self, title):
        parser = reqparse.RequestParser()
        parser.add_argument('517765d3', type=str, required=True, help='API Key is required')
        args = parser.parse_args()

        omdb_api_key = args['517765d3']
        omdb_url = f'http://www.omdbapi.com/?t={title}&apikey={omdb_api_key}'

        response = requests.get(omdb_url)

        if response.status_code == 200:
            movie_data = response.json()

            new_movie = Movie(
                title=movie_data['Title'],
                year=movie_data['Year'],
                rated=movie_data['Rated'],
                released=movie_data['Released'],
                runtime=movie_data['Runtime'],
                genre=movie_data['Genre'],
                director=movie_data['Director'],
                writer=movie_data['Writer'],
                actors=movie_data['Actors'],
                plot=movie_data['Plot'],
                language=movie_data['Language'],
                country=movie_data['Country'],
                awards=movie_data['Awards'],
                poster=movie_data['Poster'],
                imdb_rating=movie_data['imdbRating'],
                metascore=movie_data['Metascore'],
                imdb_votes=movie_data['imdbVotes'],
                imdb_id=movie_data['imdbID']
            )

            self.db.session.add(new_movie)
            self.db.session.commit()

            return {'message': 'Movie added successfully'}, 201
        else:
            return {'message': 'Movie not found'}, 404

class MovieResource(Resource):
    def __init__(self, db):
        self.db = db

    def get(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            return {
                'id': movie.id,
                'title': movie.title,
                'year': movie.year,
                'genre': movie.genre,
                'director': movie.director,
                'plot': movie.plot,
                'imdb_rating': movie.imdb_rating
                # Add more fields as needed
            }, 200
        else:
            return {'message': 'Movie not found'}, 404

    def put(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('year', type=str)
            # Add more fields as needed
            args = parser.parse_args()

            if args['title']:
                movie.title = args['title']
            if args['year']:
                movie.year = args['year']
            # Update more fields here

            self.db.session.commit()
            return {'message': 'Movie updated successfully'}, 200
        else:
            return {'message': 'Movie not found'}, 404

    def delete(self, movie_id):
        movie = Movie.query.get(movie_id)
        if movie:
            self.db.session.delete(movie)
            self.db.session.commit()
            return {'message': 'Movie deleted successfully'}, 200
        else:
            return {'message': 'Movie not found'}, 404
