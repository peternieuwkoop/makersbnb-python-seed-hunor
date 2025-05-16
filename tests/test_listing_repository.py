from lib.listing_repository import ListingRepository
from lib.listing import Listing

"""
When calling #all_listings
shows a list of Listings reflecting seed data
"""
def test_see_all_listings(db_connection):
    db_connection.seed('seeds/listings_table.sql')
    repository = ListingRepository(db_connection)

    listings = repository.all_listings()

    assert listings == [
        Listing(1, 'Country Cottage', 'Quaint little cottage with a view', 75, 'countrycottage.jpg', 1),
        Listing(2, 'Beach House', 'Well situated beachfront property', 100, 'beachhouse.jpeg', 1),
        Listing(3, 'Potato House', 'House that looks like a potato', 250, 'potato.jpg', 2)
    ]

"""
When calling #create_listing
adds a new listing which is seen calling #all_listings
"""
def test_create_new_listing(db_connection):
    db_connection.seed('seeds/listings_table.sql')
    repository = ListingRepository(db_connection)

    repository.create_listing(Listing(None, 'Stylish Flat', 'Minimalist but modern flat in the city centre', 120, 'example.jpeg', 2))

    listings = repository.all_listings()

    assert listings == [
        Listing(1, 'Country Cottage', 'Quaint little cottage with a view', 75, 'countrycottage.jpg', 1),
        Listing(2, 'Beach House', 'Well situated beachfront property', 100, 'beachhouse.jpeg', 1),
        Listing(3, 'Potato House', 'House that looks like a potato', 250, 'potato.jpg', 2),
        Listing(4, 'Stylish Flat', 'Minimalist but modern flat in the city centre', 120, 'example.jpeg', 2)
    ]

"""
when calling #find_by_user_id
returns a list of Listings made by that user_id
"""
def test_find_by_user_id(db_connection):
    db_connection.seed('seeds/listings_table.sql')
    repository = ListingRepository(db_connection)

    my_listings = repository.find_by_user_id(1)

    assert my_listings == [
        Listing(1, 'Country Cottage', 'Quaint little cottage with a view', 75, 'countrycottage.jpg', 1),
        Listing(2, 'Beach House', 'Well situated beachfront property', 100, 'beachhouse.jpeg', 1)
    ]

"""
when calling #update_listing
changes an existing Listing and calling #all_listings 
"""


"""
when calling #find_by_id
returns the correct Listing object for that id
"""
def test_find_by_id(db_connection):
    db_connection.seed('seeds/listings_table.sql')
    repository = ListingRepository(db_connection)

    listing = repository.find_by_id(1)

    assert listing == Listing(1, 'Country Cottage', 'Quaint little cottage with a view', 75, 'countrycottage.jpg', 1)
    