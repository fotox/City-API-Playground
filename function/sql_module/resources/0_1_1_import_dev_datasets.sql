-- INSERT BEAUTY SCORES
INSERT INTO dev.beauty_score (description) VALUES
    ('Ugly'),
    ('Average'),
    ('Gorgeous');

-- INSERT CITIES
INSERT INTO dev.city (city_uuid, name, geo_location_latitude, geo_location_longitude, beauty, population) VALUES
    ('311b223e-8263-4c1d-b0a8-d578444f13c8', 'City A', 40.7128, -74.0060, 1, 100000),
    ('e5a43d11-ed66-465e-b320-39b2c468cb1e', 'City B', 34.0522, -118.2437, 2, 150000),
    ('d840aa0d-8951-4c41-8b7f-32c90a88e296', 'City C', 51.5074, -0.1278, 3, 200000),
    ('375b1506-5111-4b75-939d-b2f63a1ee885', 'City D', 35.6895, 139.6917, 2, 120000),
    ('ee506bee-b6ad-447b-80d1-5649438cc11e', 'City E', -33.8688, 151.2093, 1, 180000);

-- INSERT ALLIANCES
INSERT INTO dev.alliances (city, allied_cities) VALUES
    ('311b223e-8263-4c1d-b0a8-d578444f13c8', 'e5a43d11-ed66-465e-b320-39b2c468cb1e'),
    ('311b223e-8263-4c1d-b0a8-d578444f13c8', 'd840aa0d-8951-4c41-8b7f-32c90a88e296'),
    ('e5a43d11-ed66-465e-b320-39b2c468cb1e', '375b1506-5111-4b75-939d-b2f63a1ee885'),
    ('d840aa0d-8951-4c41-8b7f-32c90a88e296', 'ee506bee-b6ad-447b-80d1-5649438cc11e');
