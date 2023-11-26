from flasgger import Swagger
from flask import Flask
from flask_basicauth import BasicAuth

from city_be.city import *
from sql_module.execution import execute_sql_by_script

API_PORT: int = 1337
INIT_DB_SCRIPT: str = 'sql_module/resources/0_0_1_init_scheme.sql'

app = Flask(__name__)

# Swagger documentation
swagger = Swagger(app, template_file='swagger.yaml')

# Init database basic authentication
load_dotenv()
app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
basic_auth = BasicAuth(app)


@app.route('/api/init_db', methods=['POST'])
@basic_auth.required
def init_database_scheme():
    return execute_sql_by_script(INIT_DB_SCRIPT)


@app.route('/api/city', methods=['GET'])
def get_cities():
    return get_city_from_database()


@app.route('/api/city/<city_id>', methods=['GET'])
def get_city(city_id: str):
    return get_city_from_database(city_id)


@app.route('/api/city', methods=['POST'])
def create_city():
    return insert_city_into_database(request.get_json())


@app.route('/api/city/<city_id>', methods=['PUT'])
def update_city(city_id: str):
    return update_city_into_database(city_id, request.get_json())


@app.route('/api/city/<city_id>', methods=['DELETE'])
def delete_city(city_id: str):
    return delete_city_from_database(city_id)


if __name__ == '__main__':
    app.run(debug=True, port=API_PORT)
