from lib.listing import Listing

class ListingRepository:

    def __init__(self, connection):
        self._connection = connection

    def all_listings(self):
        rows = self._connection.execute('SELECT * FROM listings')
        listings = []
        for row in rows:
            item = Listing(row['id'], row['name'], row['description'], row['price'], row['user_id'])
            listings.append(item)
        return listings
    
    def create_listing(self, listing):
        self._connection.execute(
            'INSERT INTO listings (name, description, price, user_id) VALUES(%s, %s, %s, %s)',
            [listing.name, listing.description, listing.price, listing.user_id]
            )
        return None
    
    def find_by_id(self, id):
        rows = self._connection.execute(
            'SELECT * FROM listings WHERE id = %s', [id]
            )
        row = rows[0]
        return Listing(row['id'], row['name'], row['description'], row['price'], row['user_id'])
    
    def find_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM listings WHERE user_id = %s', [user_id]
            )
        listings = []
        for row in rows:
            item = Listing(
                row['id'], row['name'], row['description'], row['price'], row['user_id']
                )
            listings.append(item)
        return listings
    
    def update_listing(self, update):
        self._connection.execute(
            'UPDATE listings SET ' \
            'name = %s, ' \
            'description = %s, ' \
            'price = %s ' \
            'WHERE id = %s', [update.name, update.description, update.price, update.id]
        )
    
    def delete_listing(self, id):
        self._connection.execute(
            'DELETE FROM listings WHERE id = %s', [id]
        )

