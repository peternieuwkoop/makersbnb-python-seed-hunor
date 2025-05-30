class Listing:
    
    def __init__(self, id, name, description, price, image, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.user_id = user_id

    def __repr__(self):
        return f"Listing({self.id}, {self.name}, {self.description}, {self.price}, {self.image}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__