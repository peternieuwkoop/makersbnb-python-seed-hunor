import pytest
from lib.password_validator import *

# Test valid passwords


@pytest.mark.parametrize("password", [
    "Password1!",    # Valid password
    "A$123456",      # Valid password
    "Secure!Pass9",  # Valid password
])
def test_valid_password(password):
    assert password_is_valid(password)

# Test invalid passwords due to length


@pytest.mark.parametrize("password", [
    "Short1!",   # Too short, length 7
    "12345",     # Too short, no special character or uppercase
    "abcd1234",  # Too short, no special character, no uppercase
])
def test_password_too_short(password):
    assert not password_is_valid(password)

# Test invalid passwords due to missing special character


@pytest.mark.parametrize("password", [
    "Password123",    # Missing special character
    "password1",      # Missing special character
    "NoSpecialChar1",  # Missing special character
])
def test_missing_special_character(password):
    assert not password_is_valid(password)

# Test invalid passwords due to missing uppercase letter


@pytest.mark.parametrize("password", [
    "password1!",    # Missing uppercase
    "secure!123",    # Missing uppercase
    "lowercase!1",   # Missing uppercase
])
def test_missing_uppercase(password):
    assert not password_is_valid(password)

# Test invalid passwords due to missing digit


@pytest.mark.parametrize("password", [
    "Password!!",  # Missing digit
    "Uppercase$",  # Missing digit
    "Special!char",  # Missing digit
])
def test_missing_digit(password):
    assert not password_is_valid(password)

# Test invalid passwords due to whitespace


@pytest.mark.parametrize("password", [
    "Password 1!",   # Contains whitespace
    "Secure Password!",  # Contains whitespace
])
def test_whitespace_in_password(password):
    assert not password_is_valid(password)
