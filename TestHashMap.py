from unittest import TestCase
from HashMap import HashMap


class TestHashMap(TestCase):
    def setUp(self) -> None:
        self.hashmap = HashMap()
        self.test_string = 'SEARCHEXAMPLE'
        self.unique_test_chars = TestHashMap.count_unique_chars(self.test_string)

    def test_insertion_basic(self):
        self.assertEqual(len(self.hashmap), 0)
        for index, letter in enumerate(self.test_string):
            self.hashmap[letter] = index
        self.assertEqual(len(self.hashmap), self.unique_test_chars)
        for letter in self.test_string:
            self.assertTrue(self.hashmap.defines(letter))

    def test_repeated_insertion(self):
        for number in range(100):
            self.hashmap['z'] = number
            assert self.hashmap['z'] == number
            self.assertEqual(len(self.hashmap), 1)

    def test_defines_returns_false_for_items_not_in_map(self):
        for index, letter in enumerate(self.test_string):
            self.assertFalse(self.hashmap.defines(letter))
        for index, letter in enumerate(self.test_string):
            self.hashmap[letter] = index
        for letter in 'OUTZID':
            self.assertFalse(self.hashmap.defines(letter))

    def test_defines_returns_true_for_items_in_map(self):
        for index, letter in enumerate(self.test_string):
            self.hashmap[letter] = index
        for index, letter in enumerate(self.test_string):
            self.assertTrue(self.hashmap.defines(letter))

    def test_defines_returns_false_on_deletion(self):
        index_of_delendum = int((len(self.test_string) / 2))
        delendum = self.test_string[index_of_delendum]
        for index, letter in enumerate(self.test_string):
            self.hashmap[letter] = index
        self.assertTrue(self.hashmap.defines(delendum))
        del self.hashmap[delendum]
        self.assertFalse(self.hashmap.defines(delendum))

    @staticmethod
    def count_unique_chars(string: str) -> int:
        string_to_list = list(string)
        list_to_set = set(string_to_list)
        return len(list_to_set)
