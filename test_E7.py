import pytest
import unittest
import E7

class E2Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(E7.add(3, 5), 8)
        self.assertEqual(E7.add(-3, -6), -9)

    def test_substract(self):
        self.assertEqual(E7.substract(8, 3), 5)
        self.assertEqual(E7.substract(10, -3), 13)
        
    def test_multiplay(self):
        self.assertEqual(E7.multiplay(3, 2), 6)
        self.assertEqual(E7.multiplay(-3, -8), 24)

    def test_division(self):
        self.assertEqual(E7.division(9, 3), 3)
        self.assertEqual(E7.division(-12, 4), -3)
        with pytest.raises(ZeroDivisionError):
            E7.division(3, 0)