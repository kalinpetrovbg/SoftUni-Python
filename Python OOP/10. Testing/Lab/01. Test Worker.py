class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')


import unittest

class WorkerTests(unittest.TestCase):

    def setUp(self):
        self.worker = Worker("Kalin", 3000, 100)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "Kalin")
        self.assertEqual(self.worker.salary, 3000)
        self.assertEqual(self.worker.energy, 100)

    def test_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy, old_energy + 1)

    def test_worker_with_energy_below_zero(self):
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_with_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_are_raised_after_work_method(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def tests_energy_lower_after_work_method(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy, old_energy - 1)

    def test_get_info_method_if_return_correct_values(self):
        info = self.worker.get_info()
        self.assertEqual(info, "Kalin has saved 0 money.")


if __name__ == "__main__":
    unittest.main()
