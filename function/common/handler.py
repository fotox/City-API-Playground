from flask import request, make_response, jsonify, Response


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
