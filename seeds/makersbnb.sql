DROP TABLE IF EXISTS user_table;

CREATE TABLE user_table (
    id SERIAL PRIMARY KEY,
    name text,
    email text,
    password_hash text,
    phone_number text
);

INSERT INTO user_table (name, email, password_hash, phone_number) VALUES ('Yahya', 'yahya@makers.com', '$2b$12$FoAowGlAW.fPe0YGEJl1k.x/4w5Jl1VuwvjUM3JRh8HIqBkzY.VHK', '012345678901');---password = Blahblah1!
INSERT INTO user_table (name, email, password_hash, phone_number) VALUES ('Pat', 'pat@makers.com', '$2b$12$56uPp9HDFiDsL6i3qCZO9u8Lf0nyIbut0UQrKtJg6Aja4B3mOPV.O', '012345678902'); ---password = Blahblah2!
