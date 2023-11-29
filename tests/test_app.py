import os

import pytest
import json

from log_module.log_app import viki_log

SCRIPT_PATH: str = os.path.dirname(os.path.realpath(__file__))
VALID_CITY_GET_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/valid_city_get_test_data.json'))
INVALID_CITY_GET_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/invalid_city_get_test_data.json'))
VALID_CITY_POST_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/valid_city_post_test_data.json'))
INVALID_CITY_POST_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/invalid_city_post_test_data.json'))
VALID_CITY_PUT_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/valid_city_put_test_data.json'))
INVALID_CITY_PUT_TEST_DATA = json.load(open(f'{SCRIPT_PATH}/resources/invalid_city_put_test_data.json'))


logger = viki_log("city_api")


@pytest.mark.parametrize("test_data", VALID_CITY_GET_TEST_DATA)
def test_valid_get_city(test_client, test_data):
    res = test_client.get(test_data["event"]["path"])
    assert res.status_code == int(test_data["expected"]["status"])
    assert res.json['body'] == test_data["expected"]["body"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]


@pytest.mark.parametrize("test_data", INVALID_CITY_GET_TEST_DATA)
def test_invalid_get_city(test_client, test_data):
    res = test_client.get(test_data["event"]["path"])
    assert res.json['error'] == test_data["expected"]["error"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]


@pytest.mark.parametrize("test_data", VALID_CITY_POST_TEST_DATA)
def test_valid_post_city(test_client, test_data):
    res = test_client.post(test_data["event"]["path"], json=test_data["event"]["body"])
    assert res.status_code == int(test_data["expected"]["status"])
    assert res.json['body'] == test_data["expected"]["body"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]


@pytest.mark.parametrize("test_data", INVALID_CITY_POST_TEST_DATA)
def test_invalid_post_city(test_client, test_data):
    res = test_client.post(test_data["event"]["path"], json=test_data["event"]["body"])
    assert res.json['error'] == test_data["expected"]["error"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]


@pytest.mark.parametrize("test_data", VALID_CITY_PUT_TEST_DATA)
def test_valid_put_city(test_client, test_data):
    res = test_client.put(test_data["event"]["path"], json=test_data["event"]["body"])
    assert res.status_code == int(test_data["expected"]["status"])
    assert res.json['body'] == test_data["expected"]["body"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]


@pytest.mark.parametrize("test_data", INVALID_CITY_PUT_TEST_DATA)
def test_invalid_put_city(test_client, test_data):
    res = test_client.put(test_data["event"]["path"], json=test_data["event"]["body"])
    assert res.json['error'] == test_data["expected"]["error"]
    assert res.json['status'] == int(test_data["expected"]["status"])
    assert res.json['message'] == test_data["expected"]["message"]
