from food_order import calculate_total


def test_order1():
    assert calculate_total(10, 2) == 20


def test_order2():
    assert calculate_total(15, 2) == 30


def test_order3():
    assert calculate_total(25, 4) == 100


def test_order4():
    assert calculate_total(5, 2) == 10


def test_invalid_price():
    assert calculate_total(-10, 2) == "invalid price"


def test_invalid_quantity():
    assert calculate_total(10, -2) == "invalid quantity"