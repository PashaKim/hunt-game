import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import *

example_table = [
    [55, 14, 25, 52, 21],
    [44, 31, 11, 53, 43],
    [24, 13, 45, 12, 34],
    [42, 22, 43, 32, 41],
    [51, 23, 33, 54, 15],
]
error_table = [
    ['a', 14, 25, 52, 21],
    [44, 31, 11, 53, 43],
    [24, 13, 45, 12, 34],
    [42, 22, 43, 32, 41],
    [51, 23, 33, 54, 15],
]


class TestFuncTreasureHunt(unittest.TestCase):  # functional.py
    def test_treasure_hunt_returns_list(self):
        self.assertIsInstance(treasure_hunt(example_table), list)
        self.assertIsInstance(treasure_hunt('example_table'), list)
        self.assertIsInstance(treasure_hunt(123456789), list)
        self.assertIsInstance(treasure_hunt([]), list)
        self.assertIsInstance(treasure_hunt(None), list)

        self.assertIsInstance(treasure_hunt(example_table, [11, 55, 15]), list)
        self.assertIsInstance(treasure_hunt(example_table, 'abc'), list)
        self.assertIsInstance(treasure_hunt(example_table, 123), list)
        self.assertIsInstance(treasure_hunt(example_table, []), list)
        self.assertIsInstance(treasure_hunt(example_table, None), list)


class TestObjTreasureHunt(unittest.TestCase):  # class_based.py
    def test_obj_treasure_hunt_returns_list(self):
        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map()), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt('example_table').clues_map()), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(123456789).clues_map()), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt([]).clues_map()), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(None).clues_map()), list)

        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map(), [11, 55, 15]), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map(), 'abc'), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map(), 123), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map(), []), list)
        self.assertIsInstance(treasure_hunt(TreasureHunt(example_table).clues_map(), None), list)


if __name__ == '__main__':
    unittest.main()
