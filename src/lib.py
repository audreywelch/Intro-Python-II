
class NameStorage:
    def __init__(self, name, storage = []):
        self.name = name
        self.storage = storage

class Description(NameStorage):
    def __init__(self, name, description, storage = []):
        super().__init__(name, storage = storage)
        self.description = description
        # name and storage is done for us in the parent class

    # String representation of class in the console
    # Putting it here makes our items AND our rooms have a nice output
    def __str__(self):
        return f'{self.name}\n{self.description}\n'

    def __repr__(self):
        return f'{self.name}\n{self.description}\n'