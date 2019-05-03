from lib import Description

class Item(Description):

    def __init__(self, name, description, storage = None):
        super().__init__(name, description, storage = storage)

    def on_take(self):
        print(f'You now have the {self.name} in your cart. Nice!')

    def on_drop(self):
        print(f'You have put the {self.name} back.')


