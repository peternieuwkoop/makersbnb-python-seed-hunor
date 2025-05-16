DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    password_hash text,
    phone_number text
);

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price int,
    image TEXT,
    user_id int
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id INT REFERENCES listings(id) ON DELETE CASCADE,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    user_id int,
    UNIQUE (listing_id, start_date, end_date)
);

INSERT INTO users (name, email, password_hash, phone_number) VALUES ('Yahya', 'yahya@makers.com', '$2b$12$FoAowGlAW.fPe0YGEJl1k.x/4w5Jl1VuwvjUM3JRh8HIqBkzY.VHK', '012345678901');---password = Blahblah1!
INSERT INTO users (name, email, password_hash, phone_number) VALUES ('Pat', 'pat@makers.com', '$2b$12$56uPp9HDFiDsL6i3qCZO9u8Lf0nyIbut0UQrKtJg6Aja4B3mOPV.O', '012345678902'); ---password = Blahblah2!

INSERT INTO listings (name, description, price, image, user_id) VALUES ('Country Cottage', 'Quaint little cottage with a view', 75, 'countrycottage.jpg', 1);
INSERT INTO listings (name, description, price, image, user_id) VALUES ('Beach House', 'Well situated beachfront property', 100, 'beachhouse.jpeg', 1);
INSERT INTO listings (name, description, price, image, user_id) VALUES ('Potato House', 'House that looks like a potato', 250, 'potato.jpg', 2);