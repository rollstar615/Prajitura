def create_cake(id_cake, name, description, price, calories, year):
    """
    Creates a new cake object.
    :param id_cake: the cake id, must be unique.
    :param name: the name of the cake.
    :param description: the description of the cake.
    :param price: the price.
    :param calories: the calories.
    :param year: the year the cake was added to the menu.
    :return: a cake object.
    """

    return {
        'id': id_cake,
        'name': name,
        'description': description,
        'price': price,
        'calories': calories,
        'year': year
    }


def get_id(cake):
    """
    Gets the id of a cake
    :param cake: the cake.
    :return: the cake id.
    """
    return cake['id']


def get_name(cake):
    return cake['name']


def get_description(cake):
    return cake['description']


def get_price(cake):
    return cake['price']


def get_calories(cake):
    return cake['calories']
def set_calories(cake, calories):
    cake['calories'] = calories


def get_year(cake):
    return cake['year']


def to_string(cake):
    return '{}. {}: {} - price: {}, calories: {}, year: {}'.format(
        get_id(cake),
        get_name(cake),
        get_description(cake),
        get_price(cake),
        get_calories(cake),
        get_year(cake)
    )

