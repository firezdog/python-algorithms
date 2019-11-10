from unittest import TestCase
from HashMap import HashMap


class TestHashMap(TestCase):
    def setUp(self) -> None:
        self.hashmap = HashMap()
        self.test_string = 'SEARCHEXAMPLE'
        self.hash_rep = ['Hashmap has 10/22 items:', 'E: 12', 'S: 0', 'H: 5', 'A: 8', 'M: 9', 'R: 3',
                         'C: 4', 'X: 7', 'P: 10', 'L: 11', '']
        self.unique_test_chars = TestHashMap.count_unique_chars(self.test_string)

    def insert_items(self):
        for index, letter in enumerate(self.test_string):
            self.hashmap[letter] = index

    def test_insertion_basic(self):
        self.assertEqual(len(self.hashmap), 0)
        self.insert_items()
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
        self.insert_items()
        for letter in 'OUTZID':
            self.assertFalse(self.hashmap.defines(letter))

    def test_defines_returns_true_for_items_in_map(self):
        self.insert_items()
        for index, letter in enumerate(self.test_string):
            self.assertTrue(self.hashmap.defines(letter))

    def test_defines_returns_false_on_deletion(self):
        index_of_delendum = int((len(self.test_string) / 2))
        delendum = self.test_string[index_of_delendum]
        self.insert_items()
        self.assertTrue(self.hashmap.defines(delendum))
        del self.hashmap[delendum]
        self.assertFalse(self.hashmap.defines(delendum))

    def test_str_method(self):
        self.insert_items()
        rep = self.hashmap.__str__().split('\n')
        self.assertCountEqual(rep, self.hash_rep)

    def test_resize_when_adding_items(self):
        self.insert_items()
        self.assertEqual(self.hashmap.capacity, 22)

    def test_resize_when_deleting_items(self):
        self.insert_items()
        for item in self.test_string:
            del self.hashmap[item]
        self.assertEqual(self.hashmap.capacity, 1)

    def test_raises_error_when_getting_none(self):
        with self.assertRaises(ValueError):
            self.hashmap.get(None)

    def test_raises_error_when_putting_None(self):
        with self.assertRaises(ValueError):
            self.hashmap.put(None, 3)
        with self.assertRaises(ValueError):
            self.hashmap.put(3, None)

    @staticmethod
    def count_unique_chars(string: str) -> int:
        string_to_list = list(string)
        list_to_set = set(string_to_list)
        return len(list_to_set)
