class Booking:
    
    def __init__(self, id, listing_id, start_date, end_date):
        self.id = id
        self.listing_id = listing_id
        self.start_date = start_date
        self.end_date = end_date
        
    def __repr__(self):
        return f"Request({self.id}, {self.listing_id}, {self.start_date}, {self.end_date})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__