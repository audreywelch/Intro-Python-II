from lib import Description

class Item(Description):

    def __init__(self, name, description, storage = []):
        super().__init__(name, description, storage = storage)

    def on_take(self.name):
        print(f'You have picked up {self.name}.')

    def on_drop(self.name):
        print(f'You have put the {self.name} back.')
