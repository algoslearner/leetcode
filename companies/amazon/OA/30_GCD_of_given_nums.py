'''
About
The greatest common divisor (GCD), also called the highest common factor of N numbers is the largest positive integer that divides all numbers without giving a remainder.

Write an algorithm to determine the GCD of N positive integers.

Input
The input to the function/method consists of two arguments - num, an integer representing the number of positive integers (N); arr, a list of positive integers.

Output
Return an integer representing the GCD of the given positive integers.
'''

import functools
import math


def gcd(num: int, arr: list) -> int:
    """
    :param num: The number of elements in arr.
    :param arr: The array of elements over which you want to find the GCD of.
    :return: The GCD.
    """
    return functools.reduce(math.gcd, arr)
  
 #################################################################################
# TEST

import unittest
import src.question_3

class TestQuestion3(unittest.TestCase):
    def test_question_3(self):
        num = 5
        arr = [2, 4, 6, 8, 10]
        output = 2
        self.assertEqual(src.question_3.gcd(num, arr), output)

        ## Explanation
        # The largest positive integer that divides all of the positive integers 2,4,6,8,10 without a remainder is 2.
