from collections import defaultdict

from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = defaultdict()

    def add_topping(self, topping):
        current_capacity = sum(self.__toppings.values())
        if self.__toppings_capacity > current_capacity:
            if topping not in self.__toppings:
                self.__toppings[topping.topping_type] = topping.weight
            else:
                self.__toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        total_weight = sum(self.__toppings.values())
        return total_weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, new_toppings_capacity):
        self.__toppings_capacity = new_toppings_capacity



import unittest


class Tests(unittest.TestCase):
    def test_topping_init(self):
        t = Topping("Tomato", 20)
        self.assertEqual(t._Topping__topping_type, "Tomato")
        self.assertEqual(t._Topping__weight, 20)

    def test_dough_init(self):
        d = Dough("Sugar", "Mixing", 20)
        self.assertEqual(d._Dough__flour_type, "Sugar")
        self.assertEqual(d._Dough__baking_technique, "Mixing")
        self.assertEqual(d._Dough__weight, 20)

    def test_pizza_init(self):
        d = Dough("Sugar", "Mixing", 20)
        p = Pizza("Burger", d, 5)

        self.assertEqual(p._Pizza__name, "Burger")
        self.assertEqual(p._Pizza__dough, d)
        self.assertEqual(len(p._Pizza__toppings), 0)
        self.assertEqual(p._Pizza__toppings_capacity, 5)

    def test_pizza_add_topping_error(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 0)
        with self.assertRaises(ValueError) as ctx:
            p.add_topping(t)
        self.assertEqual("Not enough space for another topping", str(ctx.exception))

    def test_pizza_add_topping_new(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 20)
        self.assertEqual(len(p.toppings), 1)

    def test_pizza_add_topping_update(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.toppings["Tomato"], 40)

    def test_pizza_calculate_total_weight(self):
        d = Dough("Sugar", "Mixing", 20)
        t = Topping("Tomato", 20)
        p = Pizza("Burger", d, 200)
        p.add_topping(t)
        p.add_topping(t)

        self.assertEqual(p.calculate_total_weight(), 60)


if __name__ == '__main__':
    unittest.main()
