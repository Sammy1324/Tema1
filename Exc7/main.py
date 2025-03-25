from Launcher import add_item
from Inventory import Inventory
from Item import Item

def main():

    name = input("Introduzca nombre del ítem: ")
    item = Item(name)
    inv = Inventory()
    if len(inv.items) < 5:
        add_item(inv.items, item.name)
    else:
        return inv.items
        
if __name__ == "__main__":
    main()