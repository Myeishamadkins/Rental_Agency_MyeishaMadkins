from core import *


def test_make_inventory_dictionary():
    inventory_list = [
        'c, computer, 100, 500, 37', 'm, movie, 5, 25, 69',
        'b, book, 10, 20, 96'
    ]

    assert make_inventory_dictionary(inventory_list) == {
        'c': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'stock': 37
        },
        'm': {
            'name': 'movie',
            'price': 5,
            'replacement fee': 25,
            'stock': 69
        },
        'b': {
            'name': 'book',
            'price': 10,
            'replacement fee': 20,
            'stock': 96
        }
    }

    inventory_list = ['1, computer, 100, 500, 50', '2, book, 10, 20, 100']

    assert make_inventory_dictionary(inventory_list) == {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'stock': 50
        },
        '2': {
            'name': 'book',
            'price': 10,
            'replacement fee': 20,
            'stock': 100
        }
    }


def test_make_money_dictionary():
    s = ['total: 58.0']
    money_list = {'total': 58.0}
    assert make_money_dictionary(s) == money_list


def test_make_money_string():
    money_dictionary = {'total': 0}
    assert make_money_string(money_dictionary) == 'total: 0'


def test_add_money():
    money_dictionary = {'total': 100}
    total = 100
    assert add_money(money_dictionary, total) == {'total': 200}


def test_take_away_money():
    money_dictionary = {'total': 100}
    deposit = 50
    assert take_away_money(money_dictionary, deposit) == {'total': 50}


def test_make_history_string():
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
        }
    }
    response = '1'
    action = 'rented'
    assert make_history_string(inventory, response,
                               action) == '\ncomputer, rented'


def test_make_inventory_string():
    inventory_dictionary = {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'stock': 50
        }
    }
    assert make_inventory_string(
        inventory_dictionary) == '1, computer, 100, 500, 50\n'


def test_in_stock():
    inventory_dictionary = {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'stock': 50
        }
    }
    item = '1'
    assert in_stock(inventory_dictionary, item)

    inventory_dictionary = {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'stock': 0
        }
    }
    item = '1'
    assert not in_stock(inventory_dictionary, item)


def test_remove_stock():
    inventory_dictionary = {
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
        }
    }

    item = '2'

    assert remove_from_stock(inventory_dictionary, item) == {
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
            'stock': 99
        }
    }


def test_replace_stock():
    inventory_dictionary = {
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
            'stock': 99
        }
    }

    item = '2'

    assert replace_stock(inventory_dictionary, item)

    inventory_dictionary == {
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
        }
    }


def test_zero_in_stock():
    inventory = {
        '1': {
            'name': 'computer',
            'price': 100,
            'replacement fee': 500,
            'deposit': 50,
            'stock': 0
        },
        '2': {
            'name': 'book',
            'price': 10,
            'replacement fee': 20,
            'deposit': 2,
            'stock': 99
        }
    }

    item = '1'

    assert zero_in_stock(inventory, item)

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
            'stock': 99
        }
    }

    assert not zero_in_stock(inventory, item)
