# opening, reading, writing, appending, and saving a file
import core


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
    print(f'Total Revenue: ${round(total, 2)}!\n')


def c_with_open_history():
    inventory = core.inventory_dictionary()
    with open("history.txt", "a") as file:
        file.write('160.5')
        file.write('\n')


def c_with_open_inventory():
    inventory = core.inventory_dictionary()
    with open('inventory.txt', 'w') as file:
        core.stock(inventory, '1')
        for item in inventory.values():
            file.write('{}, {}, {}, {}, {}'.format(
                item['name'], item['price'], item['replacement fee'],
                item['deposit'], item['stock']) + '\n')


def m_with_open_history():
    inventory = core.inventory_dictionary()
    with open("history.txt", "a") as file:
        file.write('8.57')
        file.write('\n')


def m_with_open_inventory():
    inventory = core.inventory_dictionary()
    with open('inventory.txt', 'w') as file:
        stock(inventory, '2')
        for item in inventory.values():
            file.write('{},{},{},{},{}'.format(
                item['name'], item['price'], item['replacement fee'],
                item['deposit'], item['stock']) + '\n')


def b_with_open_history():
    inventory = core.inventory_dictionary()
    with open("history.txt", "a") as file:
        file.write('13.07')
        file.write('\n')


def b_with_open_inventory():
    inventory = core.inventory_dictionary()
    with open('inventory.txt', 'w') as file:
        stock(inventory, '3')
        for item in inventory.values():
            file.write('{},{},{},{},{}'.format(
                item['name'], item['price'], item['replacement fee'],
                item['deposit'], item['stock']) + '\n')


def c_bring_back():
    with open('history.txt', 'a') as file:
        file.write('-50')
        file.write('\n')


def m_bring_back():
    with open('history.txt', 'a') as file:
        file.write('-2.5')
        file.write('\n')


def b_bring_back():
    with open('history.txt', 'a') as file:
        file.write('-2')
        file.write('\n')
