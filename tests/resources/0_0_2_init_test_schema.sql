-- DROP ALL TABLES
DROP TABLE if exists test.alliances;
DROP TABLE if exists test.city;
DROP TABLE if exists test.beauty_score;
DROP SCHEMA if exists test;

-- INITAL SCHEME
CREATE SCHEMA test;

-- CREATE BEAUTY SCORE TABLE
CREATE TABLE test.beauty_score (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

-- CREATE CITY TABLE
CREATE TABLE test.city (
    city_uuid UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    geo_location_latitude FLOAT NOT NULL,
    geo_location_longitude FLOAT NOT NULL,
    beauty INT REFERENCES test.beauty_score(id),
    population BIGINT NOT NULL
);

-- CREATE ALLIANCES TABLE
CREATE TABLE test.alliances (
    city UUID REFERENCES test.city(city_uuid),
    allied_cities UUID REFERENCES test.city(city_uuid)
);
