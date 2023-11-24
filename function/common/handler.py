from flask import request, make_response, jsonify, Response

from common.alliances_classes import *


def check_response(dataset: list, message: str) -> Response:
    if dataset:
        response = {
            'message': message,
            'method': request.method,
            'body': dataset
        }
        status_code = 200
    else:
        response = {
            'error': 'City not found',
            'method': request.method,
            'body': None
        }
        status_code = 404

    return make_response(jsonify(response), status_code)


def convert_response(city_uuid: str, name: str, geo_location_latitude: float,
                     geo_location_longitude: float, beauty: str, population: int) -> dict:
    return {
        'city_uuid': city_uuid,
        'name': name,
        'geo_location_latitude': geo_location_latitude,
        'geo_location_longitude': geo_location_longitude,
        'beauty': beauty,
        'population': population,
        'allied_cities': []
    }


def load_alliances(connection: dict, city_id: str) -> tuple[list, dict]:
    connection['cursor'].execute(SelectAlliancesData.ALLIANCES.value, (city_id, ))
    result = [row[0] for row in connection['cursor'].fetchall()]
    return result, connection


def insert_alliances(connection: dict, alliances: list, city_id) -> dict:
    for alliance_city in alliances:
        connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
            city_id,
            alliance_city
        ))
        connection['cursor'].execute(InsertAllianceData.ALLIANCES.value, (
            alliance_city,
            city_id
        ))
    connection['conn'].commit()

    return connection


def delete_alliances(connection: dict, city_id) -> dict:
    connection['cursor'].execute(DeleteAllianceData.ALLIANCES.value, (
        city_id, city_id
    ))
    connection['conn'].commit()

    return connection
