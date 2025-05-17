from lib.validator import *

def test_valid_password():
    assert password_is_valid('hello123!') == True  

def test_too_short():
    assert password_is_valid('hi1!') == False  

def test_missing_special_char():
    assert password_is_valid('hello1234') == False  

def test_missing_both():
    assert password_is_valid('hello') == False  