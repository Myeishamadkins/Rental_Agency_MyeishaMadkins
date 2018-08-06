# opening, reading, writing, appending, and saving a file
import core


def make_inventory_dictionary(inventory_list):
    inventory_dictionary = {}
    for inventory in inventory_list:
        items = inventory.split(',')
        name = items[0].strip()
        price = int(items[1].strip())
        replacement_fee = int(items[2].strip())
        stock = int(items[3].strip())
        inventory_dictionary[name] = {
            'name': name,
            'price': price,
            'replacement fee': replacement_fee,
            'stock': stock
        }

    return inventory_dictionary


def open_my_inventory():
    with open('inventory.txt') as file:
        new_file_info = file.readlines()
    return new_file_info


def write_inventory(inventory_dictionary):
    with open('inventory.txt', 'w') as file:
        inventory_string = core.make_inventory_string(inventory_dictionary)
        file.write(inventory_string)


def write_history(total):
    with open('history.txt', 'a') as file:
        file.write(str(total))
        file.write('\n')


def history():
    with open("history.txt") as file:
        history = file.read()
    print(history)


def total():
    total = 0
    filename = './history.txt'
    with open(filename) as file:
        for line in file:
            total += (float(line.strip()))
    print(f'\nTotal Revenue: ${round(total, 2)}!\n')
    print('***************************************************')
