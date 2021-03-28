from project.rooms.room import Room
from project.people.child import Child

import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Petrovi", 3000, 4)
        self.child1 = Child(5, 3)
        self.child2 = Child(10, 6)

    def test_add_children(self):                              # 1 test
        self.room.children = [self.child1, self.child2]
        self.assertEqual(self.room.children, [self.child1, self.child2])
        self.assertEqual(self.room.expenses, 0)

    def test_empty_children_list(self):                       # 2 test
        self.assertEqual(self.room.children, [])

    def test_init(self):                                      # 3 test
        self.assertEqual(self.room.family_name, "Petrovi")
        self.assertEqual(self.room.budget, 3000)
        self.assertEqual(self.room.members_count, 4)

    def test_property(self):                                  # 4 test
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))



if __name__ == "__main__":
    unittest.main()