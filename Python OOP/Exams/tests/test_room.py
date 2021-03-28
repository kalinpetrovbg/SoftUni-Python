from project.rooms.room import Room
import unittest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Petrovi", 3000, 4)

    def test_room_expenses_is_zero(self):                     # 1 test
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