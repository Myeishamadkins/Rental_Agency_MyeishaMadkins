# opening, reading, writing, appending, and saving a file
import core


def open_my_inventory():
    with open('inventory.txt') as file:
        new_file_info = file.readlines()
    return new_file_info


def write_inventory(inventory_dictionary):
    with open('inventory.txt', 'w') as file:
        inventory_string = core.make_inventory_string(inventory_dictionary)
        file.write(inventory_string)


def write_history(string):
    with open('history.txt', 'a') as file:
        file.write(string)


def history():
    with open("history.txt") as file:
        history = file.read()
    print(history)


def open_money():
    with open('money.txt') as file:
        money = file.readlines()
    return money


def write_money(string):
    with open('money.txt', 'w') as file:
        file.write(string)


def total():
    total = 0
    filename = './money.txt'
    with open(filename) as file:
        money = file.read()
    print(money)
