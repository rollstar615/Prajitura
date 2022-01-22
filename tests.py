from domain import get_id, get_name, get_description, get_price, create_cake
from logic import add_cake, update_cake, get_cake_by_id, cakes_since_given_year


def test_add_cake():
    list_of_cakes = []
    params = [3, 'jdshfjsbj', 'abc', 24, 53, 2000]
    list_of_cakes = add_cake(list_of_cakes, *params)
    assert get_id(list_of_cakes[-1]) == params[0]
    assert get_name(list_of_cakes[-1]) == params[1]
    assert get_description(list_of_cakes[-1]) == params[2]
    assert get_price(list_of_cakes[-1]) == params[3]


def test_remove_cake():
    # TODO
    pass


def test_update_cake():
    p1 = create_cake(1, 'a', 'b', 200, 100, 300)
    p2 = create_cake(13, 'b', 'd', 300, 500, 900)
    p3 = create_cake(6, 'c', 'e', 400, 600, 700)
    update_id = get_id(p3)
    update_name = 'cristi'
    update_desc = ''
    update_price = '149'
    cakes = [p1, p2, p3]
    new_cakes = update_cake(cakes, update_id, update_name, update_desc, update_price, '', 800)
    updated_cake = get_cake_by_id(new_cakes, update_id)
    assert get_name(updated_cake) == update_name
    assert get_description(updated_cake) == get_description(p3)
    assert get_price(updated_cake) == int(update_price)


def test_domain():
    c1 = create_cake(4, 'asdf', 'asdff', 30, 40, 1999)
    assert get_id(c1) == 4
    assert get_name(c1) == 'asdf'
    assert get_description(c1) == 'asdff'



def test_cakes_since_given_year():
    p1 = create_cake(1, 'a', 'b', 200, 100, 300)
    p2 = create_cake(13, 'b', 'd', 300, 500, 900)
    p3 = create_cake(6, 'c', 'e', 400, 600, 700)
    year = 400
    cakes = [p1, p2, p3]
    assert cakes_since_given_year(cakes, year) == [p2, p3]


test_add_cake()
test_remove_cake()
test_update_cake()
test_cakes_since_given_year()

test_domain()

