DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price int,
    user_id int
);

INSERT INTO listings (name, description, price, user_id) VALUES ('Country Cottage', 'Quaint little cottage with a view', 75, 1);
INSERT INTO listings (name, description, price, user_id) VALUES ('Beach House', 'Well situated beachfront property', 100, 1);
INSERT INTO listings (name, description, price, user_id) VALUES ('Potato House', 'House that looks like a potato', 250, 2);