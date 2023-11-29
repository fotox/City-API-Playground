from flask import jsonify

from log_module.log_app import viki_log
logger = viki_log("city_api")


def bad_request(error):
    logger.debug(f"Error by bad_request: {error}")
    return jsonify({'error': 'Bad Request', 'message': str(error), 'status': 400})


def unauthorized(error):
    logger.debug(f"Error by unauthorized: {error}")
    return jsonify({'error': 'Unauthorized', 'message': str(error), 'status': 401})


def forbidden(error):
    logger.debug(f"Error by forbidden: {error}")
    return jsonify({'error': 'Forbidden', 'message': str(error), 'status': 403})


def not_found(error):
    logger.debug(f"Error by not_found: {error}")
    return jsonify({'error': 'Not Found', 'message': str(error), 'status': 404})


def method_not_allowed(error):
    logger.debug(f"Error by method_not_allowed: {error}")
    return jsonify({'error': 'Method Not Allowed', 'message': str(error), 'status': 405})


def conflict(error):
    logger.debug(f"Error by conflict: {error}")
    return jsonify({'error': 'Conflict', 'message': str(error), 'status': 409})


def unsupported_media_type(error):
    logger.debug(f"Error by unsupported_media_type: {error}")
    return jsonify({'error': 'Unsupported Media Type', 'message': str(error), 'status': 415})


def unprocessable_entity(error):
    logger.debug(f"Error by unprocessable_entity: {error}")
    return jsonify({'error': 'Unprocessable Entity', 'message': str(error), 'status': 422})


def too_many_requests(error):
    logger.debug(f"Error by too_many_requests: {error}")
    return jsonify({'error': 'Too Many Requests', 'message': str(error), 'status': 429})


def internal_server_error(error):
    logger.debug(f"Error by internal_server_error: {error}")
    return jsonify({'error': 'Internal Server Error', 'message': str(error), 'status': 500})


def service_unavailable(error):
    logger.debug(f"Error by service_unavailable: {error}")
    return jsonify({'error': 'Service Unavailable', 'message': str(error), 'status': 503})
