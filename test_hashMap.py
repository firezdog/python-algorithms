from unittest import TestCase
from HashMap import HashMap


class TestHashMap(TestCase):
    def setUp(self) -> None:
        self.hashmap = HashMap()
        self.test_string = 'SEARCHEXAMPLE'

    def test_insertion(self):
        test_string = self.test_string
        unique_items_in_test_string = len(set(list(test_string)))
        hashmap = self.hashmap
        self.assertEqual(hashmap.load, 0)
        for index, letter in enumerate(test_string):
            hashmap[letter] = index
        self.assertEqual(hashmap.load, unique_items_in_test_string)
        for letter in test_string:
            self.assertTrue(hashmap.defines(letter))
        for letter in 'OUTZID':
            self.assertFalse(hashmap.defines(letter))
        for number in range(100):
            hashmap['z'] = number
            assert hashmap['z'] == number
        self.assertEqual(hashmap.load, unique_items_in_test_string + 1)
