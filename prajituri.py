'''
Functionalitati:
F1. Adaugarea unei prajituri
F2. Stergerea unei prajituri
...
Scenariu de rulare pentru F1:
# | User          | Program            | Comment
--------------------------------------------
1 |               | <meniul principal> |
2 | 1             |                    | Utilizatorul alege adaugare
3 |               | Dati ID-ul:        | Programul cere ID-ul
4 | 100           |                    | Utilizatorul da id-ul 100
5 |               | Date numele:       |
...............................................
  |               | Prajitura adaugata!|
-----------------------------------------------


Activitati pentru F1:
1. Reprezentarea prajiturii ca dictionar
2. Citirea datelor pentru o prajitura
3. Adaugarea prajiturii in colectia de prajituri
4. Finalizarea interfetei cu utilizatorul
'''
from logic import add_cake, read_from_file
from user_interface import run_ui


def main():
    list_of_cakes = read_from_file()
    list_of_cakes = run_ui(list_of_cakes)

if __name__ == '__main__':
    main()