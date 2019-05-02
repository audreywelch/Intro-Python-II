from lib import Description

# Implement a class to hold room information. This should have name and
# description attributes.

class Room(Description):

    def __init__(self, name, description, storage = []):
        super().__init__(name, description, storage = storage)
        # self.name = name
        # self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def add_item_to_room(self, new_item):
        self.storage.append(new_item)
