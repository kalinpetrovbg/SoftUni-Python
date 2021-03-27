from project.vehicle import Vehicle
import unittest

class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.car = Vehicle(63, 163)


    def test_init(self):
        self.assertEqual(self.car.fuel, 63)
        self.assertEqual(self.car.horse_power, 163)
        self.assertEqual(self.car.capacity, 63)
        self.assertEqual(self.car.fuel_consumption, 1.25)


