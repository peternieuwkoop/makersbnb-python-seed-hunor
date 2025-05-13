from lib.listing import Listing

"""
test instantiation with id, name, description, price and user_id
"""
def test_instantiation():
    listing = Listing(1, "house", "nice house", 100, 1)
    assert listing.id == 1
    assert listing.name == "house"
    assert listing.description == "nice house"
    assert listing.price == 100
    assert listing.user_id == 1

"""
test that Listing object can be formatted as a string
"""
def test_formatting():
    listing = Listing(1, "house", "nice house", 100, 1)
    assert str(listing) == "Listing(1, house, nice house, 100, 1)"

"""
test that Listings with identical attributes are equal
"""
def test_equality():
    listing1 = Listing(1, "house", "nice house", 100, 1)
    listing2 = Listing(1, "house", "nice house", 100, 1)
    assert listing1 == listing2