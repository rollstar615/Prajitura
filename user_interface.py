from domain import to_string
from logic import add_cake, remove_cake, update_cake, reduce_calories, cakes_since_given_year, max_cal_cakes_each_year, \
    sorted_by_price_over_calories


def show_menu():
    print('1. Adauga prajitura')
    print('2. Sterge prajitura')
    print('3. Modifica prajitura')
    print('4. Reducerea caloriilor pe baza de nume')
    print('5. Toate prajiturile incepand cu un an dat')
    print('6. Prajitura cu nr maxim de calorii din fiecare an')
    print('7. Prajiturile sortate dupa pret / calorii')
    print('a. Show all cakes')
    print('x. Exit')


def ui_add_cake(list_of_cakes):
    try:
        id_cake = int(input('Dati id-ul: '))
        name = input('Dati numele: ')
        description = input('Dati descrierea: ')
        price = int(input('Dati pretul: '))
        calories = int(input('Dati caloriile: '))
        year = int(input('Dati anul introducerii: '))

        new_cakes = add_cake(list_of_cakes, id_cake, name, description, price, calories, year)
        print('Cake added!')
        return new_cakes
    except ValueError as ve:
        print('Eroare:', ve)
        return list_of_cakes

def ui_show_all(list_of_cakes):
    for cake in list_of_cakes:
        print(to_string(cake))


def ui_remove_cake(list_of_cakes):
    id_cake = int(input('Dati id-ul de sters: '))
    return remove_cake(list_of_cakes, id_cake)


def ui_update_cake(list_of_cakes):
    id_cake = int(input('Dati id-ul prajiturii de actualizat: '))
    name = input('Dati noul nume, gol pentru a nu schimba: ')
    description = input('Dati noua desc, gol pentru a nu schimba: ')
    price = input('Dati noul pret, gol pentru a nu schimba: ')
    calories = input('Dati noile calorii, gol pentru a nu schimba: ')
    year = input('Dati noul an al introducerii, gol pentru a nu schimba: ')

    list_of_cakes = update_cake(
        list_of_cakes,
        id_cake,
        name,
        description,
        price,
        calories,
        year)
    print('Prajituri a fost actualizata!')
    return list_of_cakes


def ui_reduce_calories(list_of_cakes):
    search_str = input('Dati stringul de cautare: ')
    reduce_percentage = float(input('Dati procentajul de reducere (0 - 100): '))

    list_of_cakes = reduce_calories(list_of_cakes, search_str, reduce_percentage)
    print('Reducere efectuata cu succes!')
    return list_of_cakes


def ui_cakes_since_given_year(list_of_cakes):
    given_year = int(input('Dati anul:'))
    to_print = cakes_since_given_year(list_of_cakes, given_year)
    print('Prajiturile din lista incepand cu anul',given_year,'sunt:')
    for cake in to_print:
        print(to_string(cake))
    return list_of_cakes


def ui_max_cal_cakes_each_year(list_of_cakes):
   to_print = max_cal_cakes_each_year(list_of_cakes)
   for k,v in to_print.items():
       print("Pentru anul : {} avem prajitura asta : {}".format(
           k,
           to_string(v)
       ))
   return list_of_cakes


def run_ui(list_of_cakes):
    while True:
        show_menu()
        op = input('Alegeti optiunea: ')
        if op == '1':
            #list_of_cakes[:] = ...
            list_of_cakes = ui_add_cake(list_of_cakes)
        elif op == '2':
            list_of_cakes = ui_remove_cake(list_of_cakes)
        elif op == '3':
            list_of_cakes = ui_update_cake(list_of_cakes)
        elif op == '4':
            list_of_cakes = ui_reduce_calories(list_of_cakes)
        elif op == '5':
            list_of_cakes = ui_cakes_since_given_year(list_of_cakes)
        elif op == '6':
            list_of_cakes = ui_max_cal_cakes_each_year(list_of_cakes)
        elif op == '7':
            print(sorted_by_price_over_calories(list_of_cakes))
        elif op == 'a':
            ui_show_all(list_of_cakes)
        elif op == 'x':
            break

    return list_of_cakes


