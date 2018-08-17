import disk


def make_inventory_dictionary(inventory_list):
    inventory_dictionary = {}
    for inventory in inventory_list:
        items = inventory.split(',')
        key = items[0]
        value = {
            'name': items[1].strip(),
            'price': int(items[2]),
            'replacement fee': int(items[3]),
            'stock': int(items[4])
        }
        inventory_dictionary[key] = value
    return inventory_dictionary


def make_money_dictionary(money_list):
    money_dictionary = {}
    for money in money_list:
        items = money.split(':')
        key = items[0]
        value = float(items[1])
        money_dictionary[key] = value
    return money_dictionary


def make_money_string(money_dictionary):
    money_string = "total: {}".format(money_dictionary['total'])
    return money_string


def add_money(money_dictionary, total):
    money_dictionary['total'] += total
    return money_dictionary


def take_away_money(money_d'total: 0''total: 0'ictionary, deposit):
    money_dictionary['total'] -= deposit
    return money_dictionary


def make_history_string(inventory, response, action):
    history_string = f"\n{inventory[response]['name']}, {action}"
    return history_string


def make_inventory_string(inventory_dictionary):
    inventory_string = ''
    for key, value in inventory_dictionary.items():
        name = value['name']
        price = value['price']
        replacement_fee = value['replacement fee']
        stock = value['stock']
        inventory_string += '{}, {}, {}, {}, {}\n'.format(
            key, name, price, replacement_fee, stock)
    return inventory_string


def in_stock(inventory_dictionary, item):
    if inventory_dictionary[item]['stock'] > 0:
        return True
    else:
        return False


def remove_from_stock(inventory_dictionary, item):
    inventory_dictionary[item]['stock'] -= 1
    return inventory_dictionary


def replace_stock(inventory_dictionary, item):
    if item in inventory_dictionary:
        inventory_dictionary[item]['stock'] += 1
    return inventory_dictionary


def zero_in_stock(inventory, item):
    if inventory[item]['stock'] == 0:
        return True
