import disk


def inventory_dictionary():
    inventory = {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'deposit': 50,
            'stock': 50
        },
        '2': {
            'name': 'book',
            'price': 10,
            'replacement fee': 20,
            'deposit': 2,
            'stock': 100
        },
        '3': {
            'name': 'movie',
            'price': 5,
            'replacement fee': 25,
            'deposit': 2.5,
            'stock': 70
        }
    }
    return inventory


def employee_for(inventory):
    for item in inventory.values():
        print('{}, {}, {}, {}, {}'.format(item['name'], item['price'],
                                          item['replacement fee'],
                                          item['deposit'], item['stock']))


def stock(inventory_dictionary, item):
    inventory_dictionary[item]['stock'] -= 1
    return inventory_dictionary


def replace_stock(inventory_dictionary, item):
    inventory_dictionary[item]['stock'] += 1
    return inventory_dictionary


def zero_in_stock(inventory, item):
    if inventory[item]['stock'] == 0:
        return True
