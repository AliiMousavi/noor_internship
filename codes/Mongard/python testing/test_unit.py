import unittest
import unit

class TestUnit(unittest.TestCase):

    def test_add(self):
        self.assertEqual(unit.add(4,3), 7)
        self.assertEqual(unit.add(-1,5), 4)
        self.assertEqual(unit.add(4,3), 7)

    def test_subtract(self):
        self.assertEqual(unit.subtract(4,8), -4)
        self.assertEqual(unit.subtract(1,0), 1)

    def test_multiply(self):
        self.assertEqual(unit.multiply(0,4), 0)
        self.assertEqual(unit.multiply("g",4), 'gggg')

    def test_devision(self):
        self.assertEqual(unit.devision(10,5), 2)

    unittest.main()


