import os
from dotenv import load_dotenv
from flasgger import Swagger
from flask import Response, request, Flask
from flask_basicauth import BasicAuth

from common.city import get_city_from_database, insert_city_into_database, update_city_into_database, \
    delete_city_from_database, create_app
from common.error import not_found
from config import set_config
from sql_module.execution import execute_sql_by_script

# Init database basic authentication
load_dotenv()

INIT_DB_SCRIPT: str = 'sql_module/resources/0_0_1_init_prod_scheme.sql'

# Initial app
app: Flask = create_app(set_config(os.getenv('PGSCHEME')))

# Swagger documentation
swagger: Swagger = Swagger(app, template_file='../swagger.yaml')

app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
basic_auth: BasicAuth = BasicAuth(app)


@app.errorhandler(404)
def page_not_found(error):
    return not_found("Backend not found. Wrong url.")


@app.route('/api/init_db', methods=['POST'])
@basic_auth.required
def init_database_scheme() -> Response:
    return execute_sql_by_script(INIT_DB_SCRIPT)


@app.route('/api/city', methods=['GET'])
def get_cities() -> Response:
    return get_city_from_database()


@app.route('/api/city/<city_id>', methods=['GET'])
def get_city(city_id: str) -> Response:
    return get_city_from_database(city_id)


@app.route('/api/city', methods=['POST'])
def create_city() -> Response:
    return insert_city_into_database(request.get_json())


@app.route('/api/city/<city_id>', methods=['PUT'])
def update_city(city_id: str) -> Response:
    return update_city_into_database(city_id, request.get_json())


@app.route('/api/city/<city_id>', methods=['DELETE'])
def delete_city(city_id: str) -> Response:
    return delete_city_from_database(city_id)


if __name__ == '__main__':
    app.run(port=1337)
