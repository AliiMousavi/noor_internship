import unittest

class TestAbsFunction(unittest.TestCase):
    def test_posetive_number(self):
        self.assertEqual(abs(10), 10)

    def test_negetive_number(self):
        self.assertEqual(abs(-10), 10)

    def test_zero(self):
        self.assertEqual(abs(0), 0)

if __name__ == "__main__":
    unittest.main()