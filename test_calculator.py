import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -2), -3)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2,1),1)
        self.assertEqual(self.calc.subtract(-2,-1),-1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,10),20)
        self.assertEqual(self.calc.multiply(-3,5),-15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6,3),2)
        self.assertEqual(self.calc.divide(5,3),1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6,3),0)
        self.assertEqual(self.calc.modulo(5,7),5)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()