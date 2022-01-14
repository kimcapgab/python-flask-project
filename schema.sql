DROP TABLE IF EXISTS characters;

CREATE TABLE characters (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR NOT NULL,
  house_name VARCHAR NOT NULL,
  quote TEXT
);