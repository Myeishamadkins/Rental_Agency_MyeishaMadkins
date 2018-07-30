from core import *


def test_stock():
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

    item = 'book'

    assert {
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
