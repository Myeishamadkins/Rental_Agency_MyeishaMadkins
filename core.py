import disk


def make_inventory_string(inventory_dictionary):
    inventory_string = ''
    for key, value in inventory_dictionary.items():
        name = value['name']
        price = value['price']
        replacement_fee = value['replacement fee']
        stock = value['stock']
        inventory_string += '{}, {}, {}, {},\n'.format(name, price,
                                                       replacement_fee, stock)
    return inventory_string


def employee_for(inventory):
    for item in inventory.values():
        print('{}, {}, {}, {}'.format(item['name'], item['price'],
                                      item['replacement fee'], item['stock']))


def stock(inventory_dictionary, item):
    if item in inventory_dictionary.keys():
        inventory_dictionary[item]['stock'] -= 1
    return inventory_dictionary


def replace_stock(inventory_dictionary, item):
    if item in inventory_dictionary.keys():
        inventory_dictionary[item]['stock'] += 1
    return inventory_dictionary


def zero_in_stock(inventory, item):
    if inventory[item]['stock'] == 0:
        return True
