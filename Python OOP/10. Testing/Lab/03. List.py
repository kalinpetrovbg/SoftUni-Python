class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class TestIntegerList(unittest.TestCase):

    def setUp(self):
        self.ll = IntegerList([])

    def test_add_element_int(self):
        self.assertEqual(self.ll.add(5), [5])

    def test_add_non_int(self):
        self.assertRaises(ValueError, self.ll.add, "cat")

    def test_removes_element_in_range(self):
        self.ll.add(10)
        element = self.ll.remove_index(0)
        self.assertEqual(element, 10)

    def test_remove_element_out_of_range(self):
        self.assertRaises(IndexError, self.ll.remove_index, 5)

    def test_init_takes_only_integers(self):
        ll = IntegerList("cat", 15, "dog", 20)
        self.assertEqual(ll.get_data(), [15, 20])

    def test_get_in_range(self):
        self.ll.add(3)
        self.assertEqual(self.ll.get(0), 3)

    def test_get_out_of_range(self):
        self.assertRaises(IndexError, self.ll.get, 7)

    def test_insert(self):
        self.ll.add(0)
        self.ll.insert(0, 5)
        self.assertEqual(self.ll.get_data(), [5, 0])

    def test_insert_out_of_range(self):
        self.ll.add(55)
        self.assertRaises(IndexError, self.ll.insert, 1, 6)
        self.assertEqual(self.ll.get_data(), [55])

    def test_insert_string(self):
        self.ll.add(5)
        self.assertRaises(ValueError, self.ll.insert, 0, "cat")

    def test_get_biggest(self):
        self.ll.add(5)
        self.ll.add(11)
        self.assertEqual(self.ll.get_biggest(), 11)

    def test_get_index(self):
        self.ll.add(7)
        self.assertEqual(self.ll.get_index(7), 0)

if __name__ == "__main__":
    unittest.main()