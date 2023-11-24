from flask import Flask, request

from city_be.city import *
from common.handler import check_response

API_PORT = 1337
app = Flask(__name__)


@app.route('/api/city', methods=['GET'])
def get_cities():
    dataset: list = get_city_from_database()
    message: str = "Cities found successfully"
    return check_response(dataset, message)


@app.route('/api/city/<city_id>', methods=['GET'])
def get_city(city_id: str):
    dataset: list = get_city_from_database(city_id)
    message: str = "City found successfully"
    return check_response(dataset, message)


@app.route('/api/city', methods=['POST'])
def create_city():
    request_dataset: dict = request.get_json()
    dataset, message = insert_city_into_database(request_dataset)
    return check_response(dataset, message)


@app.route('/api/city/<city_id>', methods=['PUT'])
def update_city():
    dataset = request.get_json()
    return update_city_into_database(dataset)


@app.route('/api/city/<city_id>/alliance/<alliances_city_id>', methods=['POST'])
def insert_alliances(city_id: str, alliances_city_id: str):
    dataset = {'city_id': city_id, 'alliances_city_id': alliances_city_id}
    return insert_alliances_to_city(dataset)


@app.route('/api/city/<city_id>', methods=['DELETE'])
def delete_city(city_id: str):
    return delete_city_from_database(city_id)


if __name__ == '__main__':
    app.run(debug=True, port=API_PORT)
