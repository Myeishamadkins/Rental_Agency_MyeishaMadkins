# input() and print()
import core
import disk
from time import sleep


def welcome():
    print('***************************************************')
    print("Welcome to Myeisha's Rental Agency!")
    print('All items are rented for one week with a set price.')


def leave_store():
    print('\nExiting...')
    sleep(3)
    print('Exiting.....')
    sleep(2)
    print('Exiting.......\n')
    sleep(1)
    print('Goodbye, come again soon!')
    exit()


def user_employee():
    while True:
        which = input('Are you a employee? Please type [y]es, [n]o or [e]xit. '
                      ).strip().lower()
        if which == 'y' or which == 'yes':
            print('***************************************************')
            print('\n')
            return 'employee'
        elif which == 'n' or which == 'no':
            print('***************************************************')
            print('\n')
            return 'customer'
        elif which == 'e':
            return 'exit'
        else:
            print('This is not an option. Please type [y]es or [n]o. ')


def employee(inventory):
    # see stock, review transaction history, calculate total revenue.
    while True:
        choice = input(
            'Would you like to see [s]tock, review transaction [h]istory, calculate [t]otal revenue, [e]xit, or go [b]ack? '
        ).strip().lower()
        if choice == 's':
            print('***************************************************')
            employee_for(inventory)
            print('\n')
            print('***************************************************')
        elif choice == 'h':
            print('***************************************************')
            my_history()
            print('\n')
        elif choice == 't':
            print('***************************************************')
            my_total()
            print('\n')
        elif choice == 'e':
            exit()
        elif choice == 'b':
            break
        else:
            print(
                'This is not an option. Please type [s], [h], [t], [e], or [b]. '
            )


def employee_for(inventory):
    for item in inventory.values():
        print('{}, {}, {}, {}'.format(item['name'], item['price'],
                                      item['replacement fee'], item['stock']))


def my_stock(inventory_dictionary, item):
    core.stock(inventory_dictionary, item)


def my_history():
    disk.history()


def my_total():
    disk.total()
    print('***************************************************')


def user(inventory, money):
    # can rent and charge rates based on length of rentals.
    while True:
        choice = input(
            'Would you like to rent, return, or go [b]ack? ').strip().lower()
        if choice == 'rent':
            print('***************************************************')
            rent(inventory, money)
            print('\n')
        elif choice == 'return':
            print('***************************************************')
            bring_back(inventory, money)
            print('\n')
        elif choice == 'b':
            print('***************************************************')
            break
        else:
            print(
                'This is not an option. Please type rent, return, or [b]ack. ')


def printable_inventory(inventory):
    for key in inventory:
        print('name: {}, key: {}, price: {}, stock: {}'.format(
            inventory[key]['name'], key, inventory[key]['price'],
            inventory[key]['stock']))


def get_item(inventory):
    while True:
        printable_inventory(inventory)
        response = input(
            'Which item would you like to rent? Please enter key name. '
        ).lower().strip()
        print('***************************************************')
        if response in inventory:
            if core.in_stock(inventory, response):
                return response
            else:
                print('that item is out of stock! womp womp')
        else:
            print('invalid choice')


def rent(inventory, money):
    response = get_item(inventory)
    total = inventory[response]['price']
    print('Your total price will be ${:.2f}.'.format(total))
    keep = input(
        'Would you like to rent this item? Please type [y]es or [n]o. ').strip(
        ).lower()
    if keep == 'y':
        print(
            f"You have rented one {inventory[response]['name']} for one week.")
        history_string = core.make_history_string(inventory, response,
                                                  'Rented')
        core.remove_from_stock(inventory, response)
        disk.write_inventory(inventory)
        disk.write_history(history_string)
        core.add_money(money, total)
        money_string = core.make_money_string(money)
        disk.write_money(money_string)
        print('***************************************************')
        print('\n')


def bring_back(inventory, money):
    while True:
        printable_inventory(inventory)
        response = input(
            'What would you like to return? [g]o back? ').strip().lower()
        if response == 'g':
            return user(inventory, money)
            print('\n')
        elif response in inventory:
            core.replace_stock(inventory, response)
            deposit = inventory[response]['replacement fee'] * .10
            history_string = core.make_history_string(inventory, response,
                                                      'Returned')
            core.replace_stock(inventory, response)
            disk.write_history(history_string)
            core.take_away_money(money, deposit)
            money_string = core.make_money_string(money)
            disk.write_money(money_string)
        else:
            print('This is not an option. [g]o back. ')


def replace_my_stock(inventory_dictionary, item):
    core.replace_stock(inventory_dictionary, item)


def main():
    filename = './inventory.txt'
    welcome()
    inventory_list = disk.open_my_inventory()
    inventory = core.make_inventory_dictionary(inventory_list)
    money_list = disk.open_money()
    money = core.make_money_dictionary(money_list)
    while True:
        decision = user_employee()
        if decision == 'employee':
            employee(inventory)
        elif decision == 'customer':
            user(inventory, money)
        elif decision == 'exit':
            leave_store()


if __name__ == '__main__':
    main()
