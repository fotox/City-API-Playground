-- DROP ALL TABLES
DROP TABLE if exists dev.alliances;
DROP TABLE if exists dev.city;
DROP TABLE if exists dev.beauty_score;
DROP SCHEMA if exists dev;

-- INITIAL SCHEME
CREATE SCHEMA dev;

-- CREATE BEAUTY SCORE TABLE
CREATE TABLE dev.beauty_score (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255) NOT NULL
);

-- CREATE CITY TABLE
CREATE TABLE dev.city (
    city_uuid UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    geo_location_latitude FLOAT NOT NULL,
    geo_location_longitude FLOAT NOT NULL,
    beauty INT REFERENCES dev.beauty_score(id),
    population BIGINT NOT NULL
);

-- CREATE ALLIANCES TABLE
CREATE TABLE dev.alliances (
    city UUID REFERENCES dev.city(city_uuid),
    allied_cities UUID REFERENCES dev.city(city_uuid)
);
