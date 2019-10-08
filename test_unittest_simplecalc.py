from simple_calc import SimpleCalc
import unittest

class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_add2(self):
        self.assertEqual(self.calc.add(99, 5), 104)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 4), 2)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(74, 5), 69)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(17, 17), 289)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(529, 23), 23)