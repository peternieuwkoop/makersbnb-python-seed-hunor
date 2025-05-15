from lib.email_validator import *

def test_is_valid_email():
    assert email_is_valid('test@makers.com') == True
    assert email_is_valid('hello.world@domain.com') == True
    assert email_is_valid('user.name@sub.domain.com') == True

    assert email_is_valid('missingatsign.com') == False
    assert email_is_valid('@domain.com') == False
    assert email_is_valid('user@') == False
    assert email_is_valid('user@domain') == False
    assert email_is_valid('user@@domain.com') == False
    assert email_is_valid('.user@domain.com') == False