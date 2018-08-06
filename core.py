import disk

# def make_inventory_dictionary(inventory_list):
#     inventory_dictionary = {}
#     for inventory in inventory_dictionary:
#         items = inventory.split(',')
#         name = items[0].split()
#         stock = int(items[1].strip())
#         price = float(items[2].strip())
#         replacement_fee = int(items[3].strip())
#         inventory_dictionary[name] = {
#             'name': name,
#             'price': price,
#             'replacement fee': replacement_fee,
#             'stock': stock
#         }
#     return inventory_dictionary

# def open_my_inventory():
#     with open('inventory.txt') as file:
#         new_file_info = file.readlines()
#     return new_file_info


def employee_for(inventory):
    for item in inventory.values():
        print('{}, {}, {}, {}, {}'.format(item['name'], item['price'],
                                          item['replacement fee'],
                                          item['deposit'], item['stock']))


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
