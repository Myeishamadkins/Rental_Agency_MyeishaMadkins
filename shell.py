# input() and print()
# import core
# import disk


def welcome():
    print("Welcome to Myeisha's Rental Agency!")


def user_employee():
    while True:
        which = input('Are you a employee? Please type [y]es or [n]o. ').strip().lower()
        if which == 'y' or which == 'yes':

        if which == 'n' or which == 'no':

        else:
            print('This is not an option. Please type [y]es or [n]o. ')


def rental_inventory():
    inventory = {
        'Computer': {
            'Price': 100,
            'Sales Tax': .07,
            'Replacement Fee': 500,
            'Deposit': 50
        },
        'Book': {
            'Price': 10,
            'Sales Tax': .07,
            'Replacement Fee': 20,
            'Deposit': 2
        },
        'Movie': {
            'Price': 5,
            'Sales Tax': .07,
            'Replacement Fee': 25,
            'Deposit': 2.5
        }
    }


def main():
    welcome()
    user_employee()
    rental_inventory()


if __name__ == '__main__':
    main()
