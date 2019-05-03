from lib import NameStorage

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(NameStorage):

    def __init__(self, name, current_room, shopping_cart = []):
        super().__init__(name)
        #self.name = name
        self.current_room = current_room
        self.shopping_cart = shopping_cart