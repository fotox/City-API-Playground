import os
import uuid
from flask import request, jsonify, Flask
from flask_sqlalchemy import SQLAlchemy
from log_module.log_app import viki_log


API_PORT = 1337

logger = viki_log("city_api")

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = (f"postgresql://{os.environ['PGUSER']}:{os.environ['PGPASSWORD']}"
                                         f"@{os.environ['PGHOST']}:{os.environ['PGPORT']}/cities")

db = SQLAlchemy(app)


class City(db.Model):
    """
    Item model for city in backend and database
    """
    city_uuid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255))
    geo_location_latitude = db.Column(db.Float)
    geo_location_longitude = db.Column(db.Float)
    beauty = db.Column(db.Enum('Ugly', 'Average', 'Gorgeous'))
    population = db.Column(db.BigInteger)
    allied_cities = db.Column(db.ARRAY(db.String(36)))


@app.route('/api/city', methods=['GET'])
def get_city():
    city_uuid = request.args.get('city_uuid')
    if city_uuid:
        city = City.query.get(city_uuid)
        if city:
            return jsonify({
                'city_uuid': city.city_uuid,
                'name': city.name,
                'geo_location_latitude': city.geo_location_latitude,
                'geo_location_longitude': city.geo_location_longitude,
                'beauty': city.beauty,
                'population': city.population,
                'allied_cities': city.allied_cities
            })
        else:
            return jsonify({'error': 'City not found'}), 404
    else:
        cities = City.query.all()
        cities_list = [{
            'city_uuid': city.city_uuid,
            'name': city.name,
            'geo_location_latitude': city.geo_location_latitude,
            'geo_location_longitude': city.geo_location_longitude,
            'beauty': city.beauty,
            'population': city.population,
            'allied_cities': city.allied_cities
        } for city in cities]
        return jsonify(cities_list)


@app.route('/api/city', methods=['POST'])
def create_city():
    data = request.get_json()
    new_city = City(
        city_uuid=str(uuid.uuid4()),
        name=data['name'],
        geo_location_latitude=data['geo_location_latitude'],
        geo_location_longitude=data['geo_location_longitude'],
        beauty=data['beauty'],
        population=data['population'],
        allied_cities=data['allied_cities']
    )
    db.session.add(new_city)
    db.session.commit()
    return jsonify({
        'city_uuid': new_city.city_uuid,
        'name': new_city.name,
        'geo_location_latitude': new_city.geo_location_latitude,
        'geo_location_longitude': new_city.geo_location_longitude,
        'beauty': new_city.beauty,
        'population': new_city.population,
        'allied_cities': new_city.allied_cities
    }), 201


@app.route('/api/city', methods=['PUT'])
def update_city():
    data = request.get_json()
    city_uuid = data.get('city_uuid')
    if city_uuid:
        city = City.query.get(city_uuid)
        if city:
            city.name = data['name']
            city.geo_location_latitude = data['geo_location_latitude']
            city.geo_location_longitude = data['geo_location_longitude']
            city.beauty = data['beauty']
            city.population = data['population']
            city.allied_cities = data['allied_cities']
            db.session.commit()
            return jsonify({
                'city_uuid': city.city_uuid,
                'name': city.name,
                'geo_location_latitude': city.geo_location_latitude,
                'geo_location_longitude': city.geo_location_longitude,
                'beauty': city.beauty,
                'population': city.population,
                'allied_cities': city.allied_cities
            })
        else:
            return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'error': 'city_uuid not provided'}), 400


@app.route('/api/city', methods=['DELETE'])
def delete_city():
    city_uuid = request.args.get('city_uuid')
    if city_uuid:
        city = City.query.get(city_uuid)
        if city:
            db.session.delete(city)
            db.session.commit()
            return jsonify({'message': 'City deleted successfully'})
        else:
            return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'error': 'city_uuid not provided'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=API_PORT)
