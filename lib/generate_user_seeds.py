import bcrypt

# List of test users (name, email, password, phone_number)
users = [
    ("Yahya", "yahya@makers.com", "Blahblah1!", "012345678901"),
    ("Pat", "pat@makers.com", "Blahblah2!", "012345678902"),
    ("Peter", "peter@makers.com", "Blahblah3!", "12345678903")
]

print("-- SQL Seed Output")
print("TRUNCATE TABLE user_table RESTART IDENTITY;\n")

print("INSERT INTO user_table (name, email, password_hash, phone_number) VALUES")

values = []
for name, email, password, phone in users:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    sql_line = f"('{name}', '{email}', '{hashed}', '{phone}')"
    values.append(sql_line)

print(",\n".join(values) + ";")
