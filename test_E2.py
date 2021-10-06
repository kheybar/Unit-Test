import unittest
import E2

class E2Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(E2.add(3, 5), 8)
        self.assertEqual(E2.add(-3, -6), -9)

    def test_substract(self):
        self.assertEqual(E2.substract(8, 3), 5)
        self.assertEqual(E2.substract(10, -3), 13)
        
    def test_multiplay(self):
        self.assertEqual(E2.multiplay(3, 2), 6)
        self.assertEqual(E2.multiplay(-3, -8), 24)

    def test_division(self):
        self.assertEqual(E2.division(9, 3), 3)
        self.assertEqual(E2.division(-12, 4), -3)
        self.assertRaises(ZeroDivisionError, E2.division, 4, 0)


if __name__ == '__main__':
    unittest.main()