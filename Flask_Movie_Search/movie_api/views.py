from flask import Blueprint, jsonify, request
import requests
from ..settings import OMDB_API_KEY


blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/movie_search", methods=["GET"])
def movie_search():
    movie_name = request.args.get("Guardians of the Galaxy Vol. 2")
    omdb_url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"
    response = requests.get(omdb_url)
    movie_data = response.json()
    return jsonify(movie_data)
