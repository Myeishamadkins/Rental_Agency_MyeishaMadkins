# input() and print()
import core
import disk


def welcome():
    print("Welcome to Myeisha's Rental Agency!")


def user_employee():
    while True:
        which = input(
            'Are you a employee? Please type [y]es or [n]o. ').strip().lower()
        if which == 'y' or which == 'yes':
            employee()
        if which == 'n' or which == 'no':
            user()
        else:
            print('This is not an option. Please type [y]es or [n]o. ')


def open_inventory():
    inventory = open_inventory


def employee():
    # see stock, review transaction history, calculate total revenue.
    while True:
        choice = input(
            'Would you like to see [s]tock, review transaction [h]istory, or calculate [t]otal revenue? '
        )
        if choice == 's':
            stock()
        elif choice == 'h':
            history()
        elif choice == 't':
            total()
        else:
            print('This is not an option. Please type [s], [h], or [t]. ')


# def stock():


def history():
    with open("inventory.txt") as file:
        history = file.read()
    print(history)


# def total():


def user():
    # can rent and charge rates based on length of rentals.
    while True:
        choice = input('Would you like to rent or return? ')
        if choice == 'rent':
            rent()
        elif choice == 'return':
            bring_back()
        else:
            print('This is not an option. Please type rent or return. ')


def rent_function():
    while True:
        rent = input(
            'Which item would you like to rent? a [c]omputer, a [m]ovie, or a [b]ook? '
        ).lower().strip()
        if rent == 'c' or rent == 'm' or rent == 'b':
            return rent
        else:
            print(
                'This is not an option. Please select [c]omputer, [m]ovie, or [b]ook. '
            )


def rent():
    response = rent_function()
    while True:
        if response == 'c':
            print(
                'The price of a computer is $100 + $0.07 sales tax with a $50 deposit. Your total price for renting a computer will be $150.07.'
            )
            keep = input(
                'Would you like to rent a computer? Please type [y]es or [n]o. '
            )
            if keep == 'y':
                with open("history.txt", "a") as file:
                    file.write('150.07')
                    file.write('\n')
                    break
            #  elif keep == 'n':
            #     break
            else:
                print('This is not an option. Please type [y]es or [n]o.')
        if response == 'm':
            print(
                'The price of a movie is $5 + $0.07 sales tax with a $2.5 deposit. Your total price for renting a movie will be $7.57.'
            )
            keep = input(
                'Would you like to rent a movie? Please type [y]es or [n]o. ')
            if keep == 'y':
                with open("history.txt", "a") as file:
                    file.write('7.57')
                    file.write('\n')
                    break
            # elif keep == 'n':
            #     break
            else:
                print('This is not an option. Please type [y]es or [n]o.')
        if response == 'b':
            print(
                'The price of a book is $10 + $0.07 sales tax with a $2 deposit. Your total price for renting a book will be $12.07.'
            )
            keep = input(
                'Would you like to rent a book? Please type [y]es or [n]o. ')
            if keep == 'y':
                with open("history.txt", "a") as file:
                    file.write('12.07')
                    file.write('\n')
                    break
            # elif keep == 'n':
            #     break
            else:
                print('This is not an option. Please type [y]es or [n]o.')


# def bring_back():


def main():
    welcome()
    user_employee()
    inventory = my_inventory()
    function = rent_function()
    get = rent()


if __name__ == '__main__':
    main()
