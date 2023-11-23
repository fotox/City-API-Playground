from flask import request, make_response, jsonify, Response


def check_get_response(dataset: list, message: str) -> Response:
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
