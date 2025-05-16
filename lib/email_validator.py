def email_is_valid(email):
    if '@' not in email or '.' not in email:
        return False
    if email.startswith('@') or email.startswith('.') or email.endswith('@') or email.endswith('.'):
        return False
    if email.count('@') != 1:
        return False
    
    name_part, domain_part = email.split('@')
    if not name_part or not domain_part:
        return False
    if '.' not in domain_part:
        return False
    else:
        return True