from project.hardware.hardware import Hardware
from project.software.software import Software

import unittest

class TestHardware(unittest.TestCase):
    def setUp(self):
        self.h = Hardware("Lenovo", "Power", 800, 32)
        self.s = Software("Win", "Light", 10, 20)
        self.e = Software("Win", "Express", 1000, 2000)

    def test_init(self):                                    # 0 test
        self.assertEqual(self.h.name, "Lenovo")
        self.assertEqual(self.h.type, "Power")
        self.assertEqual(self.h.capacity, 800)
        self.assertEqual(self.h.memory, 32)

    def test_empty_software_components(self):               # 1 test
        self.assertEqual(self.h.software_components, [])

    def test_add_to_software_components(self):              # 2 test
        self.h.install(self.s)
        self.assertEqual(self.h.software_components, [self.s])

    def test(self):
        self.h.install(self.s)                              # 3 test
        self.assertEqual(self.h.software_components, [self.s])
        self.h.uninstall(self.s)
        self.assertEqual(self.h.software_components, [])

    def test_cannot_add_due_to_high_requirements(self):      # 4 test
        with self.assertRaises(Exception) as ex:
            self.h.install(self.e)
        self.assertEqual("Software cannot be installed", str(ex.exception))
        self.assertEqual(self.h.software_components, [])







if __name__ == "__main__":
    unittest.main()