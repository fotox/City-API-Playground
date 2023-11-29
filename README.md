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
        "375b1506-5111-4b75-939d-b2f63a1ee885"
      ],
      "allied_power": 180000,
      "beauty": "Average",
      "geo_location_latitude": 34.0522,
      "geo_location_longitude": -118.2437,
      "name": "City B",
      "population": 150000
    }
  ],
  "city_uuid": "e5a43d11-ed66-465e-b320-39b2c468cb1e",
  "message": "City found successfully",
  "status": 200
}
```

## Documentation and testing
The API is documented in Swagger and by docstrings in the functions, classes and methods.
The API is tested under `<project-root>/tests` by using pytest.


## Docker
If you want to run this API with docker, please use the Dockerfile under `<project-root>/Dockerfile`. These file
create a docker image on python-11-slim-buster base.
Similar you can run `docker-compose build` and `docker-compose up`.
!INFO! - The flask app initial the database. If its on first start failed, please use the backend call to initialized
the database.
