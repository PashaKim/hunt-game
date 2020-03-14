def matrix_to_list(matrix):
    flat_list = list()
    for row in matrix:
        flat_list = flat_list + row
    return flat_list


def treasure_hunt(table, user_clues=None):
    '''
    :param table: matrix [[,],]
    :param user_clues: list
    :return: list of clues
    '''
    try:  # check table
        int(table[0][0])
    except (TypeError, ValueError, IndexError):
        print(f'Matrix: <{table}> is wrong type, expect - [[,],[,],..] with <int> in cells')
        return []

    try:  # check user_clues
        user_clues = [int(clue) for clue in user_clues]
    except (TypeError, ValueError, IndexError):
        print('Clue has wrong type, expect - <int>. Start default:')
        user_clues = None

    clues = user_clues if (True if user_clues else False) else [table[0][0]]

    def add_clue():
        clue = clues[-1]
        coordinates = [int(digit)-1 for digit in str(clue)]  # 11 -> [1, 1]
        row, column = coordinates[0], coordinates[1]
        new_clue = table[row][column]
        if not clue == new_clue:
            clues.append(new_clue)
            add_clue()  # recursion
        else:
            print('Treasure is:', clue)

    add_clue()
    return clues
