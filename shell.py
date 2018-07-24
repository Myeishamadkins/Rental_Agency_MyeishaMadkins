# input() and print()
# import core
import disk


def welcome():
    print("Welcome to Myeisha's Rental Agency!")


def user_employee():
    while True:
        which = input('Are you a employee? Please type [y]es or [n]o. ').strip().lower()
        if which == 'y' or which == 'yes':
            employee()
        if which == 'n' or which == 'no':
            user()
        else:
            print('This is not an option. Please type [y]es or [n]o. ')

def employee():
    # see stock, review transaction history, calculate total revenue.
    while True:
        choice = input('Would you like to see [s]tock, review transaction [h]istory, or calculate [t]otal revenue? ')
        if choice == 's':
            stock()
        elif choice == 'h':
            history()
        elif choice == 't':
            total()
        else:
            print('This is not an option. Please type [s], [h], or [t]. ')

def stock():

def history():

def choice():


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

def rent():

def bring_back():

def main():
    welcome()
    user_employee()
    


if __name__ == '__main__':
    main()
