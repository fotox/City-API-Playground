-- CREATE BEAUTY SCORE TABLE
CREATE TABLE beauty_score (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

-- CREATE CITY TABLE
CREATE TABLE city (
    city_uuid UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    geo_location_latitude FLOAT NOT NULL,
    geo_location_longitude FLOAT NOT NULL,
    beauty INT REFERENCES beauty_score(id),
    population BIGINT NOT NULL
);

-- CREATE ALLIANCES TABLE
CREATE TABLE alliances (
    city UUID REFERENCES city(city_uuid),
    allied_cities UUID REFERENCES city(city_uuid)
);
