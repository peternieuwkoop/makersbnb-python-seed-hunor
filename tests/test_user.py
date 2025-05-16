from lib.user import User

"""
Define user
"""

def test_user_created():
    user = User(
        1,
        'test user',
        'test@makers.com',
        'Blahblah1!',
        '12345678901'
    )

    assert user.id == 1
    assert user.name == 'test user'
    assert user.email == 'test@makers.com'
    assert user.password_hash == 'Blahblah1!'
    assert user.phone_number == '12345678901'