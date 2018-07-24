import disk


def create_inventory_dictionary(inventory_list):
    inventory_dictionary = {}
    for inventory in inventory_list:
        items = inventory.split(',')
        key = items[0].strip()
        value = int(items[1].strip())
        inventory_dictionary[key] = value
    return inventory_dictionary
