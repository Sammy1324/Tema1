from Launcher import add_item

class Inventory:
        def __init__(self):
            self.items = []

        def add_item(self, item):
            add_item(self.items, item)

        def __repr__(self):
            return f"Inventory({self.items!r})"