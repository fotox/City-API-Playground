from flask import jsonify


def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400


def unauthorized(error):
    return jsonify({'error': 'Unauthorized', 'message': str(error)}), 401


def forbidden(error):
    return jsonify({'error': 'Forbidden', 'message': str(error)}), 403


def not_found(error):
    return jsonify({'error': 'Not Found', 'message': str(error)}), 404


def method_not_allowed(error):
    return jsonify({'error': 'Method Not Allowed', 'message': str(error)}), 405


def conflict(error):
    return jsonify({'error': 'Conflict', 'message': str(error)}), 409


def unprocessable_entity(error):
    return jsonify({'error': 'Unprocessable Entity', 'message': str(error)}), 422


def too_many_requests(error):
    return jsonify({'error': 'Too Many Requests', 'message': str(error)}), 429


def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500


def service_unavailable(error):
    return jsonify({'error': 'Service Unavailable', 'message': str(error)}), 503
