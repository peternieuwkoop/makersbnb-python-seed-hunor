#password validator
#finding email, ect.
#handles connection between user and database

from lib.user import *
from lib.database_connection import *
import bcrypt
from flask import Flask
from lib.email_validator import *


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        if not email_is_valid(user.email):
            raise ValueError('Invalid email address')
        # Hash the password
        binary_password = user.password_hash.encode('utf-8')
        password_hash = bcrypt.hashpw(binary_password, bcrypt.gensalt()).decode('utf-8')
        query = """
            INSERT INTO users (name, email, password_hash, phone_number)
            VALUES (%s, %s, %s, %s)
        """
        params = [user.name.title(), user.email.lower(), password_hash, user.phone_number]
        try:
            self._connection.execute(query, params)
        except Exception as e:
            raise ValueError(f"An error occurred while creating your account: {str(e)}")

    def all (self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows :
            person = User(
                row['id'], 
                row['name'], 
                row['email'], 
                row['password_hash'],
                row['phone_number'])
            users.append(person)
        return users

    def find_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        params = [email.lower()]
    
        cursor = self._connection.execute(query, params)
    
        # Iterate over the cursor
        for row in cursor:
            return User(
                row['id'],
                row['name'],
                row['email'],
                row['password_hash'],
                row['phone_number']
            )
    
        # If no user found, return None
        return None
    
    