def add_item(inventory, item):
    while True:
        if item in inventory:
            raise ValueError(f"El item '{item}' ya está en el inventario.")
        else:
            inventory.append(item)

        if len(inventory) > 5:
            return inventory