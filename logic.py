from copy import deepcopy

from domain import create_cake, get_id, get_name, get_description, get_price, set_calories, get_calories, get_year
import json


def save_to_file(list_of_cakes):
    '''
    Saves a list of cakes to file as json.
    :param list_of_cakes: the list of cakes
    :return: -
    '''
    with open('prajituri.txt', 'w') as f_out:
        f_out.write(json.dumps(list_of_cakes))


def read_from_file():
    '''
    Reads a list of cakes from a file containing json
    :return: a list of cakes
    '''
    try:
        with open('prajituri.txt', 'r') as f_in:
            return json.loads(f_in.read())
    except FileNotFoundError:
        return []


def get_cake_by_id(list_of_cakes, id_cake):
    """
    Gets a cake with a given id.
    :param list_of_cakes: the list of cakes.
    :param id_cake: the ID to search for.
    :return: a cake with id=id_cake
    """

    for cake in list_of_cakes:
        if get_id(cake) == id_cake:
            return cake
    return None


def add_cake(list_of_cakes, id_cake, name, description, price, calories, year):
    """
    Adds a new cake.
    :param list_of_cakes: the current list of list_of_cakes.
    :param id_cake: the cake id.
    :param name: the cake name.
    :param description: the description.
    :param price: the price.
    :param calories: the calories.
    :param year: the year.
    :return: a new list of list_of_cakes, with the new cake added to its end.
    """

    if get_cake_by_id(list_of_cakes, id_cake) is not None:
        raise ValueError('Exista deja o prajitura cu id-ul {}'.format(id_cake))


    #for cake in list_of_cakes:
    #    if get_id(cake) == id_cake:
    #        raise ValueError('Exista deja o prajitura cu id-ul {}'.format(id_cake))

    new_cake = create_cake(id_cake, name, description, price, calories, year)
    # [cake1, cake2, ..., caken] + [new_cake] => [cake1, ..., caken, new_cake]
    result = list_of_cakes + [new_cake]
    save_to_file(result)
    return result

def remove_cake(list_of_cakes, id_cake):
    """
    :param list_of_cakes:
    :param id_cake:
    :return:
    """

    # TODO: if no cake with id=id_cake, raise ValueError

    return [cake for cake in list_of_cakes if get_id(cake) != id_cake]

    # new_list = []
    # for cake in list_of_cakes:
    #     if get_id(cake) != id_cake:
    #         new_list.append(cake)
    # return new_list


def update_cake(list_of_cakes, id_cake, name, description, price, calories, year):
    """
    Updates a cake by id.
    Empty string for a parameter means that it won't be changed.
    :param list_of_cakes: the current list of cakes
    :param id_cake: the id of the cake to update.
    :param name: the new name.
    :param description: the new description.
    :param price: str, the new price.
    :param calories: str, the new calories.
    :param year: str, the new year.
    :return: a list of cakes, with the given cake updated.
    """
    new_cakes = []
    for cake in list_of_cakes:
        if get_id(cake) != id_cake:
            new_cakes.append(cake)
        else:
            new_cake = create_cake(
                get_id(cake),
                name if name != '' else get_name(cake),
                description if description != '' else get_description(cake),
                int(price) if price != '' else get_price(cake),
                'TODO',
                'TODO'
            )
            new_cakes.append(new_cake)
    return new_cakes


def reduce_calories(list_of_cakes, search_str, reduce_percentage):
    """
    Reduces the number of calories by a percentage for each cake
    containing a given string in its name.
    :param list_of_cakes: the list of cakes.
    :param search_str: the string to select cakes by.
    :param reduce_percentage: float,
            the percentage to reduce the calories by.
            Between 0.0 and 100.0
    :return: a new list of cakes with the updated calories.
    """

    updated_cakes = deepcopy(list_of_cakes)
    for cake in updated_cakes:
        if search_str in get_name(cake):
            changed_calories = (100 - reduce_percentage) * get_calories(cake) / 100
            set_calories(cake, changed_calories)

    return updated_cakes


def cakes_since_given_year(list_of_cakes, start_year):
    """
    Determina prajiturile de dupa un an dat.
    :param list_of_cakes: lista de prajituri.
    :param start_year: anul de inceput.
    :return: o lista cu prajiturile introduse in meniu incepand cu start_year
    """
    result = [cake for cake in list_of_cakes if get_year(cake) >= start_year]
    return result


def max_cal_cakes_each_year(list_of_cakes):
    """
    Determina prajitura cu nr maxim de calorii pentru fiecare an.
    :param list_of_cakes: lista de prajituri.
    :return: un dictionar d, d[k] = prajitura cu calorii maxime din anul k
    """

    '''
    Exemplu:
    p1: an=100, cal=200
    p2: an=200, cal=300
    p3: an=100, cal=100
    p4: an=200, cal=400

    cake = p1:
        year_cakes = {100: p1}
    cake = p2:
        year_cakes = {100: p1, 200: p2}
    cake = p3:
        year_cakes = {100: p1, 200: p2}
    cakes = p4:
        year_cakes = {100: p1, 200: p4}
    '''
    year_cakes = {}
    for cake in list_of_cakes:
        year = get_year(cake)
        calories = get_calories(cake)
        if year in year_cakes:
            if get_calories(year_cakes[year]) < calories:
                year_cakes[year] = cake
        else:
            year_cakes[year] = cake
    return year_cakes


def sorted_by_price_over_calories(list_of_cakes):
    def my_key(cake):
       return get_price(cake) / get_calories(cake)

    return sorted(list_of_cakes, key=my_key)


