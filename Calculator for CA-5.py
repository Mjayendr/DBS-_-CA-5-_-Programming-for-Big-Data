# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 20:23:36 2017
This is a program for different calculator functions 
@author: Jay Monpara
Student ID - 10360474
Email - 10360474@mydbs.ie
"""
import unittest
import math

class Calculator(object):
 
    def add(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return reduce(lambda a,b: a+b, x)
            else:
                raise ValueError

    def subtract(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return reduce(lambda a,b: a-b, x)
            else:
                raise ValueError

    def multiply(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return reduce(lambda a,b: a * b, x)
            else:
                raise ValueError

    def square(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return map(lambda a : a**2, x)
            else:
                raise ValueError

    def square_route(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return map(lambda a : a**(1.0/2), x)
            else:
                raise ValueError
        

    def divide(self, x):
        number_types = (int, long, float, complex)
        for number in x:
            if number != number_types:
                return reduce(lambda a,b: a/ b, x)
            else:
                raise ValueError


    def factorial(self, x):
        number_types = (int)
        for n in x:
            if n != number_types:
                return map(lambda a: math.factorial(a), x)
        else:
            raise ValueError

    def log(self, x):
         number_types = (int, float)
         for n in x:
            if n != number_types:
                return map(lambda a: math.log10(a), x)
            else:
                raise ValueError

    def xpowery(self, x, y):
         return map(lambda x,y : x**y, x,y)

    def percent(self, x, y):
         return map(lambda x,y: (x * y ) / 100, x,y)
        

# test the calculator functionality
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

	# this tests the add functionality for the list of numbers
	# 1 + 2 +3 + 4 = 10
	# 2 + 4 + (-2) = 4
	# 2 + (-2) = 0
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add([1,2,3,4])
        self.assertEqual(10, result)
        result = self.calc.add([2,4,-2])
        self.assertEqual(4, result)
        result = self.calc.add([2, -2])
        self.assertEqual(0, result)

    # This tests subtract functionality for a list of numbers
    # 2 - (-4) = 6
    # 10-5-3 = 2
    def test_calculator_subtract_method_returns_correct_result(self):
        result = self.calc.subtract([10,5,3])
        self.assertEqual(2, result)
        result = self.calc.subtract([2,-4])
        self.assertEqual(6, result)
        result = self.calc.subtract([2,-4,0,3])
        self.assertEqual(3, result)

    # This tests multiply functionality
    # 2 * 2 * 5= 20
    # 2 *(- 4) * 5 = -40
    # 2 * 0 * 5 = 0
    def test_calculator_multiply_method_returns_correct_result(self):
        result = self.calc.multiply([2,2,5])
        self.assertEqual(20, result)
        result = self.calc.multiply([2, -4, 5])
        self.assertEqual(-40, result)
        result = self.calc.multiply([2, 0, 5])
        self.assertEqual(0, result)

    # testing for square functionality for a list
    def test_calculator_square_method_returns_correct_result(self):
        result = self.calc.square([2,4])
        self.assertEqual([4,16], result)
        result = self.calc.square([1,2,3,0])
        self.assertEqual([1,4,9,0], result)
        result = self.calc.square([-4,15])
        self.assertEqual([16, 225], result)

    # Square root functionality testing for a list
    def test_calculator_square_route_method_returns_correct_result(self):
        result = self.calc.square_route([4,9])
        self.assertEqual([2,3], result)
        result = self.calc.square_route([0, 100, 25])
        self.assertEqual([0,10,5], result)
        
    # Divide functionality testing for a list.
    def test_calculator_divide_returns_correct_result(self):
        result = self.calc.divide([4, 2])
        self.assertEqual(2, result)
        result = self.calc.divide([9, 2.0, 4.5])
        self.assertEqual(1, result)
        result = self.calc.divide([-8, 5.0])
        self.assertEqual(-1.6 , result)

    # Factorials Functinality testing for a list of numbers.
    def test_calculator_factorial_returns_correct_result(self):
        result = self.calc.factorial([1,2,3,4])
        self.assertEqual([1,2,6,24], result)
        result = self.calc.factorial([5,0])
        self.assertEqual([120,1], result)

    # log functionality testing for a list.
    def test_calculator_log_returns_correct_result(self):
        result = self.calc.log([10,100,1])
        self.assertEqual([1,2,0], result)


    # testing for x ^ y for lists of numbers
    def test_calculator_xpowery_returns_correct_result(self):
        result = self.calc.xpowery([1,2,3], [1,2,3])
        self.assertEqual([1,4,27], result)
        result = self.calc.xpowery([10,5,0], [5,0,1])
        self.assertEqual([100000,1,0], result)


    # testing of percentage functionality for a list of numbers
    def test_calculator_percent_method_returns_correct_result(self):
        result = self.calc.percent([8,6,30], [2.0,50.0, -10.0])
        self.assertEqual([0.16,3,-3], result)
        

if __name__ == '__main__':
    unittest.main()
