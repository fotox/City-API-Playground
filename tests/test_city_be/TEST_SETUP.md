# Setup testcase
```json
[
  {
    "description": "",
    "event": {
      "httpMethod": "GET",
      "path": "/api/city/57a70e1b-8896-4302-a4ab-30c728971337",
      "pathParameters": {
        "asset_type": "city",
        "asset_id": "57a70e1b-8896-4302-a4ab-30c728971337"
      }
    },
    "expected": {
      "status": 200,
      "body": {
            "allied_cities": [
                "e5a43d11-ed66-465e-b320-39b2c468cb1e",
                "d840aa0d-8951-4c41-8b7f-32c90a88e296"
            ],
            "beauty": "Ugly",
            "city_uuid": "311b223e-8263-4c1d-b0a8-d578444f13c8",
            "geo_location_latitude": 40.7128,
            "geo_location_longitude": -74.006,
            "name": "City A",
            "population": 100000
        }
      }
    }
  }
]
```

# Update in app.py

```python
def lambda_handler(event: dict, context: dict) -> dict:
    http_method_str: str = event.get('httpMethod')
    resource_str = event.get("resource")

    if event.get('pathParameters') is None:
        return
    asset_type = event.get('pathParameters', {}).get('asset_type')
    asset_id = event.get('pathParameters', {}).get('asset_id')

    try:
        http_method = Method(http_method_str)
        resource = Resource(resource_str)
    except ValueError:
        return error_response(HTTPStatus.BAD_REQUEST, ValidationError("Invalid resource path"), path)

    request_type: RequestType = (http_method, resource)

    return request_type
```

# Context test_app.py

```python
import pytest
from unittest.mock import patch
from city_be.sql_module.connection import connect_to_postgres

VALID_GET_TEST_DATA = json.loads(
    files("tests.city_be.resources").joinpath("valid_city_get_list.json").read_text())


@pytest.fixture
def db_mock():
    with patch("functions.sql_module.connection.connect_to_postgres") as mock_connect:
        mock_connection = {"cursor": None, "conn": None}
        mock_connect.return_value = mock_connection
        yield mock_connection


@pytest.mark.parametrize("test_data", VALID_GET_TEST_DATA)
def test_get(db_mock, test_data):
    event = test_data.get("event")

    from city_be.app import lambda_handler

    actual = lambda_handler(event, context=None)

    expected = test_data.get("expected")
    assert actual.get("statusCode") == expected.get("status")

    actual_body = json.loads(actual.get("body"))
    assert actual_body == expected.get("body")
```
