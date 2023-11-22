import uuid

from flask import Flask, jsonify

from city_be.city import *
from log_module.log_app import viki_log

logger = viki_log("city_api")

API_PORT = 1337

app = Flask(__name__)


@app.route('/api/city', methods=['GET'])
def get_cities():
    return get_city_from_database()


@app.route('/api/city/<city_id>', methods=['GET'])
def get_city(city_id: str):
    return get_city_from_database(city_id)


@app.route('/api/city', methods=['POST'])
def create_city():
    dataset: dict = {
        "beauty": "Average",
        "city_uuid": uuid.uuid4(),
        "geo_location_latitude": 34.0522,
        "geo_location_longitude": -118.2437,
        "name": "City B",
        "population": 150000
    }
    return insert_city_into_database(dataset)


@app.route('/api/city', methods=['PUT'])
def update_city():
    pass


@app.route('/api/city/<city_id>', methods=['DELETE'])
def delete_city(city_id: str):
    return delete_city_from_database(city_id)


if __name__ == '__main__':
    app.run(debug=True, port=API_PORT)
