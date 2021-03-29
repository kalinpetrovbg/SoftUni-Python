from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory
import unittest

class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.p = PaintFactory("Factory", 100)

    def test_init(self):                                # 1 test
        self.assertEqual(self.p.name, "Factory")
        self.assertEqual(self.p.capacity, 100)

    def test_add_wrong_type(self):                      # ?
        self.assertEqual(self.p.ingredients, {})
        with self.assertRaises(TypeError) as ex:
            self.p.add_ingredient("purple", 10)
        self.assertEqual(f"Ingredient of type purple not allowed in PaintFactory", str(ex.exception))
        self.assertEqual(self.p.ingredients, {})

    def test_to_high_requirements(self):                # 2, 3, 5 test
        self.assertEqual(self.p.ingredients, {})
        with self.assertRaises(ValueError) as ex:
            self.p.add_ingredient("white", 200000)
        self.assertEqual(f"Not enough space in factory", str(ex.exception))

    def test_add_successfully(self):                    # 4 test
        self.assertEqual(self.p.ingredients, {})
        self.p.add_ingredient("white", 1)
        self.assertEqual(self.p.ingredients, {"white": 1})

    def test_remove_successfully(self):                 # 6 test
        self.p.add_ingredient("white", 4)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.p.remove_ingredient("white", 1)
        self.assertEqual(self.p.ingredients, {"white": 3})

    def test_remove_to_zero(self):
        self.p.add_ingredient("white", 4)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.p.remove_ingredient("white", 4)
        self.assertEqual(self.p.ingredients, {"white": 0})

    def test_remove_non_existing(self):                          # ????????????
        self.p.add_ingredient("white", 10)
        with self.assertRaises(Exception) as ex:
            self.p.remove_ingredient("whites", 100)
        self.assertEqual(self.p.ingredients, {"white": 10})
        self.assertEqual(Exception, "No such product in the factory")

    def test_remove_non_existing_ver_2(self):
        self.p.add_ingredient("white", 10)
        self.assertRaises(KeyError, self.p.remove_ingredient,"whites", 100)
        self.assertEqual(self.p.ingredients, {"white": 10})

    def test_remove_bigger_quantity_than_exists(self):
        self.p.add_ingredient("white", 10)
        with self.assertRaises(ValueError) as ex:
            self.p.remove_ingredient("white", 100)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(ex.exception))
        self.assertEqual(self.p.ingredients, {"white": 10})

    def test_property(self):
        self.p.ingredients = {}
        self.assertEqual(self.p.ingredients, {})

    def test_can_add_parent_method(self):
        self.assertEqual(self.p.ingredients, {})
        self.p.add_ingredient("white", 4)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.p.can_add(10)
        self.p.add_ingredient("blue", 10)
        self.assertEqual(self.p.ingredients, {"white": 4, "blue": 10})


if __name__ == "__main__":
    unittest.main()