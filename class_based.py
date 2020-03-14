class TreasureHunt:
    def __init__(self, table, user_clues=None):
        try:  # check user_clues
            user_clues = [int(clue) for clue in user_clues]
        except (TypeError, ValueError, IndexError):
            print('Clue has wrong type, expect - <int>. Start default:')
            user_clues = None

        try:  # check table
            int(table[0][0])
        except (TypeError, ValueError, IndexError):
            print(f'Matrix: <{table}> is wrong type, expect - [[,],[,],..] with <int> in cells')
            self.error = True

        self.table = table
        self.clues = user_clues if (True if user_clues or self.error else False) else [table[0][0]]

    treasure_cell = None
    error = False

    def matrix_to_list(self):
        table_list = list()
        for row in self.table:
            table_list = table_list + row
        return table_list

    def next_clue(self, clue):
        '''
        :param clue: int 
        :return: new_clue: int
        '''
        coordinates = [int(digit) - 1 for digit in str(clue)]  # 11 -> [1, 1]
        row, column = coordinates[0], coordinates[1]
        return self.table[row][column]

    def clues_map(self):
        if self.error:
            return []

        while not self.treasure_cell:
            clue = self.clues[-1]
            new_clue = self.next_clue(clue)
            if clue == new_clue:
                self.treasure_cell = new_clue
            else:
                self.clues.append(new_clue)
        return self.clues
