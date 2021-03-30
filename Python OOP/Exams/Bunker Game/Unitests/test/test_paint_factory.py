from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory

import unittest

class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.p = PaintFactory("Factory", 100)

    def test_init(self):                                 # 1 test
        self.assertEqual(self.p.name, "Factory")
        self.assertEqual(self.p.capacity, 100)
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})

    def test_which_are_valid(self):
        self.assertEqual(self.p.valid_ingredients, ['white', 'yellow', 'blue', 'green', 'red'])

    def test_change_the_valid_pieces(self):
        self.assertEqual(self.p.valid_ingredients, ['white', 'yellow', 'blue', 'green', 'red'])
        self.p.valid_ingredients = ['blackish']
        self.assertEqual(self.p.valid_ingredients, ['blackish'])

    def test_add_successfully(self):                     # 2, 3, 4, 5 test
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 1)
        self.assertEqual(self.p.ingredients, {"white": 1})
        self.assertEqual(self.p.products, {"white": 1})
        self.p.add_ingredient("white", 0)
        self.assertEqual(self.p.ingredients, {"white": 1})
        self.assertEqual(self.p.products, {"white": 1})

    def test_add_all_successfully(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 1)
        self.p.add_ingredient("yellow", 1)
        self.p.add_ingredient("blue", 1)
        self.p.add_ingredient("green", 1)
        self.p.add_ingredient("red", 1)
        self.assertEqual(self.p.ingredients, {"white": 1, "yellow": 1, "blue": 1, "green": 1, "red": 1})
        self.assertEqual(self.p.products, {"white": 1, "yellow": 1, "blue": 1, "green": 1, "red": 1})

    def test_add_zero(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 0)
        self.assertEqual(self.p.ingredients, {"white": 0})
        self.assertEqual(self.p.products, {"white": 0})

    def test_products_and_capacity(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.assertEqual(self.p.capacity, 100)
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 5)
        self.assertEqual(self.p.products, {"white": 5})
        self.assertEqual(self.p.ingredients, {"white": 5})
        self.assertEqual(self.p.capacity, 100)

    def test_remove_successfully(self):                  # 6 test
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        self.p.remove_ingredient("white", 1)
        self.assertEqual(self.p.ingredients, {"white": 3})
        self.assertEqual(self.p.products, {"white": 3})
        self.p.remove_ingredient("white", 3)
        self.assertEqual(self.p.ingredients, {"white": 0})
        self.assertEqual(self.p.products, {"white": 0})










    def test_can_add_true(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        self.assertEqual(self.p.can_add(10), True)
        self.p.add_ingredient("white", 10)
        self.assertEqual(self.p.ingredients, {"white": 14})
        self.assertEqual(self.p.products, {"white": 14})

    def test_can_add_false(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        self.assertEqual(self.p.can_add(100000), False)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.assertEqual(self.p.products, {"white": 4})

    def test_not_allowed(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        black = "cheren"
        with self.assertRaises(TypeError) as ex:
            self.p.add_ingredient(black, 5)
        expected = str(ex.exception)
        actual = f"Ingredient of type {black} not allowed in PaintFactory"
        self.assertEqual(expected, actual)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.assertEqual(self.p.products, {"white": 4})

    def test_not_enough_space(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        with self.assertRaises(ValueError) as ex:
            self.p.add_ingredient("white", 4000000)
        expected = str(ex.exception)
        actual = "Not enough space in factory"
        self.assertEqual(expected, actual)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.assertEqual(self.p.products, {"white": 4})

    def test_remove_non_existing_ingredient(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        with self.assertRaises(KeyError) as ex:
            self.p.remove_ingredient("blackmagic", 5)
        expected = str(ex.exception)
        actual = "\'No such product in the factory\'"
        self.assertEqual(expected, actual)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.assertEqual(self.p.products, {"white": 4})

    def test_remove_ingredient_with_less_than_zero(self):
        self.assertEqual(self.p.ingredients, {})
        self.assertEqual(self.p.products, {})
        self.p.add_ingredient("white", 4)
        with self.assertRaises(ValueError) as ex:
            self.p.remove_ingredient("white", 400)
        expected = str(ex.exception)
        actual = "Ingredient quantity cannot be less than zero"
        self.assertEqual(expected, actual)
        self.assertEqual(self.p.ingredients, {"white": 4})
        self.assertEqual(self.p.products, {"white": 4})


if __name__ == "__main__":
    unittest.main()