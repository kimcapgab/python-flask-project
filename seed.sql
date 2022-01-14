
TRUNCATE TABLE CHARACTERS;

ALTER SEQUENCE characters_id_seq RESTART WITH 1;


INSERT INTO characters (fullname, house_name, quote) VALUES ('Jon Snow', 'House Stark of Winterfell', 'If I fall, don''t bring me back.');
