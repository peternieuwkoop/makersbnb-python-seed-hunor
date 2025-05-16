from lib.listing import Listing
from datetime import datetime, timedelta


class ListingRepository:

    def __init__(self, connection):
        self._connection = connection

    def all_listings(self):
        rows = self._connection.execute('SELECT * FROM listings')
        listings = []
        for row in rows:
            item = Listing(
                row['id'], row['name'], row['description'],
                row['price'], row['image'], row['user_id']
            )
            listings.append(item)
        return listings

    def create_listing(self, listing):
        self._connection.execute(
            '''
            INSERT INTO listings (name, description, price, image, user_id)
            VALUES (%s, %s, %s, %s, %s)
            ''',
            [listing.name, listing.description, listing.price, listing.image, listing.user_id]
        )
        return None

    def find_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM listings WHERE user_id = %s', [user_id]
        )
        listings = []
        for row in rows:
            item = Listing(
                row['id'], row['name'], row['description'],
                row['price'], row['image'], row['user_id']
            )
            listings.append(item)
        return listings

    def find_by_id(self, listing_id):
        rows = self._connection.execute(
            'SELECT * FROM listings WHERE id = %s', [listing_id]
        )

        for row in rows:
            return Listing(
                row['id'], row['name'], row['description'],
                row['price'], row['image'], row['user_id']
            )
        return None
    
    def get_booked_dates(self, listing_id):
        rows = self._connection.execute(
            'SELECT start_date, end_date FROM bookings WHERE listing_id = %s',
            [listing_id]
        )
        booked_dates = []
        for row in rows:
            start_date = row['start_date']  # already a datetime.date object
            end_date = row['end_date']
            current = start_date
            while current <= end_date:
                booked_dates.append(current.strftime('%Y-%m-%d'))  # convert to string here
                current += timedelta(days=1)
        return booked_dates
    
    def create_booking(self, listing_id, start_date, end_date, user_id):
        rows = self._connection.execute("""
            SELECT 1 FROM bookings
            WHERE listing_id = %s AND (
                (start_date <= %s AND end_date >= %s) OR
                (start_date <= %s AND end_date >= %s) OR
                (start_date >= %s AND end_date <= %s)
            )
        """, [listing_id, start_date, start_date, end_date, end_date, start_date, end_date])
    
    # If rows is not empty, it means there is a booking conflict
        if rows:
            return False

        self._connection.execute("""
            INSERT INTO bookings (listing_id, start_date, end_date, user_id)
            VALUES (%s, %s, %s, %s)
        """, [listing_id, start_date, end_date, user_id])
    
        return True
    
    def create_booking_request(self, listing_id, start_date, end_date, user_id):
        self._connection.execute("""
            INSERT INTO requests (listing_id, requester_id, start_date, end_date)
            VALUES (%s, %s, %s, %s)
        """, [listing_id, start_date, end_date, user_id])
        return True
    
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