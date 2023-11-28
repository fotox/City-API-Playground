import uuid

import pytest

from common.process import convert_city_response, calculate_distance


def test_convert_city_response_with_valid_data():
    """

    :return: None
    """
    city_uuid = str(uuid.uuid4())
    name = "TestCity"
    geo_location_latitude = 40.7128
    geo_location_longitude = -74.0060
    beauty = "A"
    population = 1000000

    expected_result = {
        'city_uuid': city_uuid,
        'name': name,
        'geo_location_latitude': geo_location_latitude,
        'geo_location_longitude': geo_location_longitude,
        'beauty': beauty,
        'population': population,
        'allied_cities': []
    }

    result = convert_city_response(city_uuid, name, geo_location_latitude,
                                   geo_location_longitude, beauty, population)

    assert result == expected_result


def test_calculate_allied_power():
    # TODO:
    pass


def test_calculate_distance():
    """

    :return:
    """
    source = (40.7128, -74.0060)
    destination = (34.0522, -118.2437)

    expected_result = 3932.29727215671

    result = calculate_distance(source, destination)
    assert result.km == pytest.approx(expected_result, rel=1e-2)
