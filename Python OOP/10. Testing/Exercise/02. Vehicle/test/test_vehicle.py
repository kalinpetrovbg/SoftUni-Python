from project.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(63, 163)

    def test_init(self):
        self.assertEqual(self.car.fuel, 63)
        self.assertEqual(self.car.horse_power, 163)
        self.assertEqual(self.car.capacity, 63)
        self.assertEqual(self.car.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_out_of_reach(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(self.car.fuel, 63)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_in_range(self):
        self.car.drive(4)
        self.assertEqual(self.car.fuel, 58)

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(100)
        self.assertEqual(self.car.fuel, 63)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_car_refuel(self):
        self.car.drive(40)
        self.car.refuel(7)
        self.assertEqual(self.car.fuel, 20)

    def test_str(self):
        self.assertEqual(self.car.__str__(), f"The vehicle has 163 horse power with 63 "
                                             f"fuel left and 1.25 fuel consumption")

