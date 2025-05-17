def password_is_valid(password):
    if len(password) < 8:
        return False
    
    special_characters = {'!', '@', '$', '%', '&'}

    if not any(char in special_characters for char in password):
        return False
    
    else:
        return True