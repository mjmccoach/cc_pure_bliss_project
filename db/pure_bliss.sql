DROP TABLE IF EXISTS bucketlist;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    continent VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE bucketlist (
    id SERIAL PRIMARY KEY,
    city_id INT REFERENCES cities(id) on DELETE CASCADE,
    country_id INT REFERENCES countries(id) on DELETE CASCADE,
    visited BOOLEAN
);