# Flask City Api

## Description
The `CityApi` is a RESTFUL API managing Cities and their metadata with CRUD calls and persists the information in a
postgres instance.

## CRUD
### CREATE
When creating a City all values, but its own uuid can be passed along. The uuid is supposed to be generated internally
on city creation and returned in the creation response. All fields are mandatory, but allied_cities allows a Null
value or an empty list.

### UPDATE
Anything but the uuid of a city (which is used for pathing in the restful api) can be updated (also multiple values
at once). Updating the allied_cities is supposed to FULLY REPLACE the alliances in both directions.

### DELETE
Deletion will fully remove a city and will also remove it as an ally from all former allies

### GET
The Api is supposed to allow for both, retrival of a single city by UUID or all cities.


## Request and response formats
### Request
```http request
http(s)://<IP/DOMAIN>:1337/api/<CALL>/<SUBCALL>
```

### Response
```json
{
    "body": [
        {
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
    ],
    "message": "City found successfully",
    "method": "GET"
}
```

## Documentation and testing
The API is documented in Swagger and by docstrings in the functions, classes and methods.
The API is tested under `<project-root>/tests` by using pytest.
