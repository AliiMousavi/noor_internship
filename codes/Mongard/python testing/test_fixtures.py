import unittest
from fixtures import Person

class TestFixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.p1 = Person("Amir", "Big")
        cls.p2 = Person("john", "low")

    @classmethod
    def tearDown(cls):
        del cls.p1
        del cls.p2

    def test_full_name(self):
        self.assertEqual(self.p1.full_name(), "Amir Big")
        self.assertEqual(self.p1.email(), "AmirBig@gmail.com")


    def test_email(self):
        self.assertEqual(self.p1.email(), "AmirBig@gmail.com")

    unittest.main()


