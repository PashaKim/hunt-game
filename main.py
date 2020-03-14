from class_based import TreasureHunt
from functional import treasure_hunt

example_table = [
    [55, 14, 25, 52, 21],
    [44, 31, 11, 53, 43],
    [24, 13, 45, 12, 34],
    [42, 22, 43, 32, 41],
    [51, 23, 33, 54, 15],
]

task_table = [
    [34, 21, 32, 41, 25],
    [14, 42, 43, 14, 31],
    [54, 45, 52, 42, 23],
    [33, 15, 51, 31, 35],
    [21, 52, 33, 13, 22],
]


def start():
    print('Hi!')
    table_type = input('>Select table: E - example[55, 14, 25...] or T - task[34, 21, 32...] :')
    table = task_table if table_type == 'T' else example_table

    print('Matrix:')
    for row in table:
        print(row)

    clues = input('>Pass or select clues like: 11, 55, 15 :').split(',')
    if clues == ['']:
        print("You doesn't select clue.")
        clues = None
    else:
        print(f'You select clues:{clues}')

    method = input('>Select method: F - functional or C - class based:')
    if method == 'F':
        print('You select "Functional" method.')
        print(treasure_hunt(table, clues))
    elif method == 'C':
        print('You select "Class based" method.')
        hunt = TreasureHunt(table, clues)
        clues = hunt.clues_map()
        print(hunt.clues_map())
        if clues:
            print('Treasure is:', hunt.treasure_cell)
    else:
        print("You doesn't select (F - functional or C - class based)")


if __name__ == '__main__':
    start()
