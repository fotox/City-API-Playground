import pytest
import json

VALID_TEST_DATA = json.load(open('resources/valid_test_cities.json'))


@pytest.mark.parametrize("test_data", VALID_TEST_DATA)
def test_get_city(test_client, test_data):
    res = test_client.get(test_data["event"]["path"])
    assert res.status_code == int(test_data["expected"]["status"])
    assert res.json['body'] == test_data["expected"]["body"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]
