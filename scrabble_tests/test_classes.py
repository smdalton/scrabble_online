import unittest
from scrabble import ScrabbleBoard

class ScrabbleBoardTestCase(unittest.TestCase):

    def setUp(self):
        self.board = ScrabbleBoard()

    def test_reset_bag(self):
        for i in range(10):
            before = len(self.board.bag)
            self.board.reset_bag()
            after = len(self.board.bag)
            self.assertEqual(before,after)

    def test_get_hand_with_zero(self):
        get_zero = self.board.get_hand(0)
        self.assertEqual(len(get_zero), 0, f"{get_zero} tiles causing error")

    def test_get_hand_with_1(self):
        self.board.reset_bag()
        get_one = self.board.get_hand(1)
        self.assertEqual(len(get_one), 1, f" {get_one} is not get one ")


    def test_get_hand_with_8(self):
        self.board.reset_bag()
        get_eight = self.board.get_hand(8)
        self.assertEqual(get_eight, -1, f" {get_eight} is not get one ")


