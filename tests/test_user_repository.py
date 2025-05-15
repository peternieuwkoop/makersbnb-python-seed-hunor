from lib.user_repository import *
from lib.user import *
import pytest
import bcrypt


"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_user_repo_starts_empty(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed('seeds/makersbnb.sql') # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new ArtistRepository
    user = repository.all() # Get all artists
    assert user == [
        User(1, 'Yahya', 'yahya@makers.com', '$2b$12$FoAowGlAW.fPe0YGEJl1k.x/4w5Jl1VuwvjUM3JRh8HIqBkzY.VHK', '012345678901'),
        User(2, 'Pat', 'pat@makers.com', '$2b$12$56uPp9HDFiDsL6i3qCZO9u8Lf0nyIbut0UQrKtJg6Aja4B3mOPV.O', '012345678902')
    ]

# """
# When we call UserRepository#all
# We get a list of User objects reflecting the seed data.
# """
# def test_user_repo_starts_all(db_connection):
#     db_connection.seed('seeds/makersbnb.sql') 
#     repository = UserRepository(db_connection) 
#     user = repository.all() 

#     assert user == [
#         User('Yahya', 'yahya@makers.com', 'Blahblah1!', '012345678901'),
#         User('Pat', 'pat@makers.com', 'Blahblah2!', '012345678902')
#     ]

"""
When we call UserRepository#create
We get a new record in the database.
"""

def test_create_user(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = UserRepository(db_connection)

    new_user = User(None, 'Peter', 'peter@makers.com', 'Blahblah3!', '12345678903')
    repository.create(new_user)
    result = repository.all()
    user = result[-1]
    assert user.name == 'Peter'
    assert user.email == 'peter@makers.com'
    assert bcrypt.checkpw("Blahblah3!".encode("utf-8"), user.password_hash.encode("utf-8"))
    assert user.phone_number == '12345678903'

def test_create_another_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    new_user = User(None, 'Olly', 'Olly@makers.com', 'Blahblah4!', '12345678904')
    repository.create(new_user)
    result = repository.all()
    user = result[-1]
    assert user.name == 'Olly'
    assert user.email == 'olly@makers.com'
    assert bcrypt.checkpw('Blahblah4!'.encode('utf-8'), user.password_hash.encode('utf-8'))
    assert user.phone_number == '12345678904'

""""
Testing creation with invalid email
"""

def test_create_user_with_invalid_email(db_connection):
    db_connection.seed('seeds/makersbnb.sql')  
    repository = UserRepository(db_connection)

    invalid_user = User(None, 'Bob', 'invalidemail.com', 'Blahblah9!', '01234567899')

    with pytest.raises(ValueError) as error:
        repository.create(invalid_user)

    assert str(error.value) == 'Invalid email address'

""""
Testing creation with valid email
"""

def test_create_user_with_valid_email(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = UserRepository(db_connection)

    # Create a user with a valid email
    valid_user = User(None, 'Sam', 'sam@makers.com', 'Blahblah5!', '01234567895')

    # Create the user in the database
    repository.create(valid_user)

    # Retrieve the user from the DB and check the fields
    result = repository.all()
    created_user = result[-1]  # The last user inserted

    assert created_user.name == 'Sam'
    assert created_user.email == 'sam@makers.com'
    assert created_user.phone_number == '01234567895'
    
    # Check that the password matches after hashing
    assert bcrypt.checkpw('Blahblah5!'.encode('utf-8'), created_user.password_hash.encode('utf-8'))
