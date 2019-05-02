from lib import Description

class Item(Description):

    def __init__(self, name, description, storage = []):
        super().__init__(name, description, storage = storage)

