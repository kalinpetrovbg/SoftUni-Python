class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "320d", 5, 63)

    def test_init(self):
        self.assertEqual(self.car.make, "BMW")
        self.assertEqual(self.car.model, "320d")
        self.assertEqual(self.car.fuel_consumption, 5)
        self.assertEqual(self.car.fuel_capacity, 63)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make(self):
        self.car.make = "Audi"
        self.assertEqual(self.car.make, "Audi")

    def test_empty_make(self):
        with self.assertRaises(Exception):
            self.car.make = ""

    def test_model(self):
        self.car.model = "330d"
        self.assertEqual(self.car.model, "330d")

    def test_empty_model(self):
        with self.assertRaises(Exception):
            self.car.model = ""

    def test_fuel_consumption(self):
        self.car.fuel_consumption = 1
        self.assertEqual(self.car.fuel_consumption, 1)
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_fuel_capacity(self):
        self.car.fuel_capacity = 1
        self.assertEqual(self.car.fuel_capacity, 1)
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1

    def test_fuel_amount(self):
        self.car.fuel_amount = 1
        self.assertEqual(self.car.fuel_amount, 1)
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel_negative(self):
        self.assertRaises(Exception, self.car.refuel, -10)

    def test_refuel(self):
        old_fuel = self.car.fuel_amount
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, old_fuel + 10)

    def test_refuel_but_full(self):
        self.car.fuel_capacity = 101
        self.car.fuel_amount = 100
        self.car.refuel(500)
        self.assertRaises(Exception, self.car.fuel_amount, 101)

    def test_drive_with_enough_fuel(self):
        self.car.fuel_consumption = 5
        self.car.fuel_amount = 100
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 95)

    def test_drive_without_enough_fuel(self):
        self.car.fuel_consumption = 5
        self.car.fuel_amount = 4
        self.assertRaises(Exception, self.car.drive, 100)


if __name__ == "__main__":
    unittest.main()