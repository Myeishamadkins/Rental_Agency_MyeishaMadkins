# input() and print()
# import core
# import disk


def welcome():
    print('***************************************************')
    print("Welcome to Myeisha's Rental Agency!")


def user_employee(inventory):
    while True:
        which = input(
            'Are you a employee? Please type [y]es or [n]o. ').strip().lower()
        if which == 'y' or which == 'yes':
            print('***************************************************')
            employee(inventory)
        if which == 'n' or which == 'no':
            print('***************************************************')
            user()
        else:
            print('This is not an option. Please type [y]es or [n]o. ')


# core.py
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


def employee(inventory):
    # see stock, review transaction history, calculate total revenue.
    while True:
        choice = input(
            'Would you like to see [s]tock, review transaction [h]istory, calculate [t]otal revenue, [e]xit, or go [b]ack? '
        ).strip().lower()
        if choice == 's':
            print('***************************************************')
            for item in inventory.values():
                print('{}, {}, {}, {}, {}'.format(
                    item['name'], item['price'], item['replacement fee'],
                    item['deposit'], item['stock']))
            print('***************************************************')
        elif choice == 'h':
            print('***************************************************')
            history()
        elif choice == 't':
            print('***************************************************')
            total()
        elif choice == 'e':
            exit()
        elif choice == 'b':
            return
        else:
            print(
                'This is not an option. Please type [s], [h], [t], [e], or [b]. '
            )


# core.py
def stock(inventory_dictionary, item):
    inventory_dictionary[item]['stock'] -= 1
    return inventory_dictionary


# disk.py
def history():
    with open("history.txt") as file:
        history = file.read()
    print(history)


# disk.py
def total():
    total = 0
    filename = './history.txt'
    with open(filename) as file:
        for line in file:
            total += (float(line.strip()))
    print(f'Total Revenue: ${round(total, 2)}!\n')


def user():
    # can rent and charge rates based on length of rentals.
    inventory = inventory_dictionary()
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
            return
        else:
            print(
                'This is not an option. Please type rent, return, or [b]ack. ')


def rent_function():
    while True:
        rent = input(
            'Which item would you like to rent? A [c]omputer, a [m]ovie, a [b]ook, or [g]o back? '
        ).lower().strip()
        print('***************************************************')
        if rent == 'c' or rent == 'm' or rent == 'b' or rent == 'g':
            return rent
        else:
            print(
                'This is not an option. Please select [c]omputer, [m]ovie, or [b]ook. '
            )


def rent(inventory):
    response = rent_function()
    # filename = './inventory.txt'
    # file_string = core.create_inventory_string(inventory)
    # disk.write_file(filename, file_string)
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
                # disk.py
                # new function(with open)
                with open("history.txt", "a") as file:
                    file.write('160.5')
                    file.write('\n')
                    print(
                        '***************************************************')
                with open('inventory.txt', 'w') as file:
                    stock(inventory, '1')
                    for item in inventory.values():
                        file.write('{}, {}, {}, {}, {}'.format(
                            item['name'], item['price'],
                            item['replacement fee'], item['deposit'],
                            item['stock']) + '\n')
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
                # disk.py
                # new function(with open)
                print('You have rented one movie for one week.')
                with open("history.txt", "a") as file:
                    file.write('8.57')
                    file.write('\n')
                    print('\n')
                with open('inventory.txt', 'w') as file:
                    stock(inventory, '2')
                    for item in inventory.values():
                        file.write('{},{},{},{},{}'.format(
                            item['name'], item['price'],
                            item['replacement fee'], item['deposit'],
                            item['stock']) + '\n')
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
                # disk.py
                # new function(with open)
                with open("history.txt", "a") as file:
                    file.write('13.07')
                    file.write('\n')
                    print(
                        '***************************************************')
                with open('inventory.txt', 'w') as file:
                    stock(inventory, '3')
                    for item in inventory.values():
                        file.write('{},{},{},{},{}'.format(
                            item['name'], item['price'],
                            item['replacement fee'], item['deposit'],
                            item['stock']) + '\n')
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
    while True:
        back = input(
            'What would you like to return? A [c]omputer, a [m]ovie, a [b]ook, or [g]o back? '
        )
        if back == 'c':
            replace_stock(inventory, '1')
            # disk.py
            # new function(with open)
            with open('history.txt', 'a') as file:
                file.write('-50')
                file.write('\n')
                print('***************************************************')
            return
        elif back == 'm':
            replace_stock(inventory, '2')
            # disk.py
            # new function(with open)
            with open('history.txt', 'a') as file:
                file.write('-2.5')
                file.write('\n')
                print('***************************************************')
            return
        elif back == 'b':
            replace_stock(inventory, '3')
            # disk.py
            # new function(with open)
            with open('history.txt', 'a') as file:
                file.write('-2')
                file.write('\n')
                print('***************************************************')
            return
        elif back == 'g':
            return
        else:
            print(
                'This is not an option. Please select A [c]omputer, a [m]ovie, a [b]ook, or [g]o back. '
            )


def replace_stock(inventory_dictionary, item):
    inventory_dictionary[item]['stock'] += 1
    return inventory_dictionary


def main():
    filename = './inventory.txt'
    welcome()
    inventory = inventory_dictionary()
    user_employee(inventory)
    function = rent_function()
    get = rent()


if __name__ == '__main__':
    main()
