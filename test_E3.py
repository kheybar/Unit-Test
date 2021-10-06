# unittest

import unittest 
from E3 import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Mahdi', 'Zarepour')
        self.p2 = Person('Rose', 'Ziba')

    def tearDown(self):
        print('Done')

    def test_fullname(self):
        self.assertEqual(self.p1.fullname(), 'Mahdi Zarepour')
        self.assertEqual(self.p2.fullname(), 'Rose Ziba')

    def test_email(self):
        self.assertEqual(self.p1.email(), 'MahdiZarepour@gmail.com')
        self.assertEqual(self.p2.email(), 'RoseZiba@gmail.com')




if __name__ == '__main__':
    unittest.main()