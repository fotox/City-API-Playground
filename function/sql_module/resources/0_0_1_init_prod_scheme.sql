-- DROP ALL TABLES
DROP TABLE if exists prod.alliances;
DROP TABLE if exists prod.city;
DROP TABLE if exists prod.beauty_score;
DROP SCHEMA if exists prod;

-- INITIAL SCHEME
CREATE SCHEMA prod;

-- CREATE BEAUTY SCORE TABLE
CREATE TABLE prod.beauty_score (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

-- CREATE CITY TABLE
CREATE TABLE prod.city (
    city_uuid UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    geo_location_latitude FLOAT NOT NULL,
    geo_location_longitude FLOAT NOT NULL,
    beauty INT REFERENCES prod.beauty_score(id),
    population BIGINT NOT NULL
);

-- CREATE ALLIANCES TABLE
CREATE TABLE prod.alliances (
    city UUID REFERENCES prod.city(city_uuid),
    allied_cities UUID REFERENCES prod.city(city_uuid)
);
