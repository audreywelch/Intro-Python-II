from lib import NameStorage

# Write a class to hold player information, e.g. what room they are in
# currently.

class Player(NameStorage):

    def __init__(self, name, current_room, storage = []):
        super().__init__(name, storage = storage)
        self.current_room = current_room
        # self.name = name
        # self.item_bag = []