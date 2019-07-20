"""
Narcissistic Number on codewars

A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
1^3 + 5^3 + 3^3 = 153

Write a method is_narcissistic(i) (in Haskell: isNarcissistic :: Integer -> Bool) which returns whether or not i is a Narcissistic Number.
"""

import math
import unittest

def is_narcissistic(value):
    org_value = value
    length = int(math.floor(math.log10(value)+1))
    num_list=list()

    for i in range(length):
        u = length-i-1
        num = (int)(value/(10**u))
        value = value-((10**u)*num)
        num_list.append(num)
    narc_value = sum(map(lambda x: x**length, num_list))

    if narc_value == org_value:
        return True
    else:
        return False

class testValidity(unittest.TestCase):
    """Tests for Narcissistic Number"""
    def testifequals(self):
        self.assertEqual(is_narcissistic(153), True)
        self.assertEqual(is_narcissistic(201), False)
        self.assertEqual(is_narcissistic(259), False)
        self.assertEqual(is_narcissistic(371), True)
        self.assertEqual(is_narcissistic(407), True)
        self.assertEqual(is_narcissistic(595), False)
        self.assertEqual(is_narcissistic(825), False)
        self.assertEqual(is_narcissistic(1634), True)

if __name__ == '__main__':
    unittest.main()

