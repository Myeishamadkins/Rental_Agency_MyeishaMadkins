# input() and print()
import core
import disk


def welcome():
    print('***************************************************')
    print("Welcome to Myeisha's Rental Agency!")
    print('All items are rented for one week with a set price.')


def user_employee(inventory):
    while True:
        which = input('Are you a employee? Please type [y]es, [n]o or [e]xit. '
                      ).strip().lower()
        if which == 'y' or which == 'yes':
            print('***************************************************')
            employee(inventory)
        if which == 'n' or which == 'no':
            print('***************************************************')
            user()
        if which == 'e':
            exit()
        else:
            print('This is not an option. Please type [y]es or [n]o. ')


def my_inventory():
    disk.make_inventory_dictionary(inventory_list)


def employee(inventory):
    # see stock, review transaction history, calculate total revenue.
    while True:
        choice = input(
            'Would you like to see [s]tock, review transaction [h]istory, calculate [t]otal revenue, [e]xit, or go [b]ack? '
        ).strip().lower()
        if choice == 's':
            print('***************************************************')
            core.employee_for(inventory)
            print('***************************************************')
        elif choice == 'h':
            print('***************************************************')
            my_history()
        elif choice == 't':
            print('***************************************************')
            my_total()
        elif choice == 'e':
            exit()
        elif choice == 'b':
            return user_employee(inventory)
        else:
            print(
                'This is not an option. Please type [s], [h], [t], [e], or [b]. '
            )


def my_stock(inventory_dictionary, item):
    core.stock(inventory_dictionary, item)


def my_history():
    disk.history()


def my_total():
    disk.total()


def user():
    # can rent and charge rates based on length of rentals.
    inventory_list = disk.open_my_inventory()
    inventory = disk.make_inventory_dictionary(inventory_list)
    while True:
        choice = input(
            'Would you like to rent, return, or go [b]ack? ').strip().lower()
        if choice == 'rent':
            print('***************************************************')
            rent(inventory)
        elif choice == 'return':
            print('***************************************************')
            bring_back(inventory)
        elif choice == 'b':
            print('***************************************************')
            return user_employee(inventory)
        else:
            print(
                'This is not an option. Please type rent, return, or [b]ack. ')


def rent_function():
    inventory_list = disk.open_my_inventory()
    inventory_dictionary = disk.make_inventory_dictionary(inventory_list)
    while True:
        rent = input(
            'Which item would you like to rent? A [c]omputer, a [m]ovie, a [b]ook, or [g]o back? '
        ).lower().strip()
        print('***************************************************')
        if rent == 'c' or rent == 'm' or rent == 'b':
            return rent
        elif rent == 'g':
            return user()
        else:
            print(
                'This is not an option. Please select [c]omputer, [m]ovie, or [b]ook. '
            )


def rent(inventory):
    response = rent_function()
    inventory_list = disk.open_my_inventory()
    inventory_dictionary = disk.make_inventory_dictionary(inventory_list)
    while True:
        if response == 'c':
            print(
                'The price of a computer is $100 + $0.07 sales tax with a $50 deposit. Your total price for renting a computer will be $160.5.'
            )
            print('***************************************************')
            keep = input(
                'Would you like to rent a computer? Please type [y]es, [n]o, or go [b]ack. '
            ).strip().lower()
            if keep == 'y':
                print('You have rented one computer for one week.')
                total = 160.5
                disk.write_history(total)
                print('***************************************************')
                print('\n')
                core.stock(inventory_dictionary, 'computer')
                disk.write_inventory(inventory_dictionary)
                break
            elif keep == 'n':
                break
            elif keep == 'b':
                return
            else:
                print(
                    'This is not an option. Please type [y]es, [n]o, or go [b]ack.'
                )

        if response == 'm':
            print(
                'The price of a movie is $5 + $0.07 sales tax with a $2.5 deposit. Your total price for renting a movie will be $8.57.'
            )
            print('***************************************************')
            keep = input(
                'Would you like to rent a movie? Please type [y]es, [n]o, or go [b]ack. '
            ).strip().lower()
            if keep == 'y':
                print('You have rented one movie for one week.')
                total = 8.57
                disk.write_history(total)
                print('***************************************************')
                print('\n')
                disk.write_inventory(inventory_dictionary)
                break
            elif keep == 'n':
                break
            elif keep == 'b':
                return
            else:
                print(
                    'This is not an option. Please type [y]es, [n]o, or go [b]ack.'
                )
        if response == 'b':
            print(
                'The price of a book is $10 + $0.07 sales tax with a $2 deposit. Your total price for renting a book will be $13.07.'
            )
            print('***************************************************')
            keep = input(
                'Would you like to rent a book? Please type [y]es, [n]o, or go [b]ack. '
            ).strip().lower()
            if keep == 'y':
                print('You have rented one book for one week.')
                total = 13.07
                disk.write_history(total)
                print('***************************************************')
                print('\n')
                disk.write_inventory(inventory_dictionary)
                break
            elif keep == 'n':
                break
            elif keep == 'b':
                return
            else:
                print(
                    'This is not an option. Please type [y]es, [n]o, or go [b]ack.'
                )


def bring_back(inventory):
    inventory_information = disk.open_my_inventory()
    inventory_dictionary = disk.make_inventory_dictionary(
        inventory_information)
    while True:
        back = input(
            'What would you like to return? A [c]omputer, a [m]ovie, a [b]ook, or [g]o back? '
        ).strip().lower()
        if back == 'c':
            replace_my_stock(inventory_dictionary, 'computer')
            total = -50
            disk.write_history(total)
            disk.write_inventory(inventory_dictionary)
            print('Here is your $50.00 deposit back.\nPlease come again!')
            print('***************************************************')
            return
        elif back == 'm':
            replace_my_stock(inventory_dictionary, 'movie')
            total = -2.5
            disk.write_history(total)
            disk.write_inventory(inventory_dictionary)
            print('Here is your $2.50 deposit back.\nPlease come again!')
            print('***************************************************')
            return
        elif back == 'b':
            replace_my_stock(inventory_dictionary, 'book')
            total = -2
            disk.write_history(total)
            disk.write_inventory(inventory_dictionary)
            print('Here is your $2.00 deposit back.\nPlease come again!')
            print('***************************************************')
            return
        elif back == 'g':
            return
        else:
            print(
                'This is not an option. Please select A [c]omputer, a [m]ovie, a [b]ook, or [g]o back. '
            )


def replace_my_stock(inventory_dictionary, item):
    core.replace_stock(inventory_dictionary, item)


def main():
    filename = './inventory.txt'
    welcome()
    inventory_list = disk.open_my_inventory()
    inventory = disk.make_inventory_dictionary(inventory_list)
    user_employee(inventory)
    function = rent_function()
    get = rent()


if __name__ == '__main__':
    main()
