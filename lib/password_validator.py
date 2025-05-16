import re

def password_is_valid(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one special character
    special_characters = {'!', '@', '$', '%', '&'}
    if not any(char in special_characters for char in password):
        return False

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Optional: Check for whitespace (if you don't want spaces in the password)
    if any(char.isspace() for char in password):
        return False

    return True