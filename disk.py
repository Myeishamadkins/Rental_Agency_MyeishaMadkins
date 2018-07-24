# opening, reading, writing, appending, and saving a file
# import core
# import test_core


def rental_inventory():
    with open('inventory.txt') as file:
        file.readlines()
    return file.readlines
