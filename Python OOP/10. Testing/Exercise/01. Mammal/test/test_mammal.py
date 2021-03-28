from project.mammal import Mammal

import unittest

class TestMammal(unittest.TestCase):
    def setUp(self):
        self.animal = Mammal("Tiger", "cats", "GRR")

    def test_init(self):
        self.assertEqual(self.animal.name, "Tiger")
        self.assertEqual(self.animal.type, "cats")
        self.assertEqual(self.animal.sound, "GRR")

    def test_private_attribute(self):
        self.assertEqual(self.animal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.animal.make_sound(), "Tiger makes GRR")

    def test_get_kingdom(self):
        self.assertEqual(self.animal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.animal.info(), "Tiger is of type cats")


if __name__ == "__main__":
    unittest.main()