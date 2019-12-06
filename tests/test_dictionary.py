import unittest
from classes.scrabble_dictionary import Dictionary


class ScrabbleBoardTestCase(unittest.TestCase):

    def setUp(self):
        self.dictionary = Dictionary()
        self.real_word = 'cheeseburger'
        self.fake_word = 'garblesnashtick'

    def test_word_exists(self):
        self.assertEqual(self.dictionary.word_exists(self.real_word), True)
        self.assertEqual(self.dictionary.word_exists(self.fake_word), False)

    def test_word_has_definition(self):
        self.assertNotEqual(self.dictionary.word_definition(self.real_word), None, f"The word should have a definition")
        self.assertEqual(self.dictionary.word_definition(self.fake_word), None, 'The word should have no definition')

    def test_fail(self):
        self.assertEqual(1,2,"dictionary fail test")


