from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import requests

app = Flask(__name__)
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)
api = Api(app)

class MovieSearch(Resource):
    def get(self, title):
        omdb_api_key = 'YOUR_OMDB_API_KEY'  # Replace with your actual API key
        omdb_url = f'https://www.omdbapi.com/?t={title}&apikey={omdb_api_key}'
        response = requests.get(omdb_url)

        if response.status_code == 200:
            movie_data = response.json()
            return movie_data, 200
        else:
            return {'message': 'Movie not found'}, 404

api.add_resource(MovieSearch, '/movie/<string:title>')

if __name__ == '__main__':
    app.run(debug=True)

