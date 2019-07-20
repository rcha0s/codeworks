'''
Valid Phone Number on codewars

Write a function that accepts a string, and returns true if it is in the form of a phone number. 
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses) 

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false
'''

import re
import unittest


def validPhoneNumber(phoneNumber):
	reg_pattern=r'^\([0-9]{3,4}\)[\s]?[0-9]{3}[-\s]?[0-9]{4}$'
	'''
	Kept failing with the input (123) 456-7890abc. Realized that match function only checks at the beginning 
	of everyline and does not care what comes after the match. So, for exact match we got to use anchors ^ and $.
	'''
	z=re.match(reg_pattern,phoneNumber)

	if z:
		return True
	else:
		return False

class testValidity(unittest.TestCase):
	def testiftrue(self):
		self.assertTrue(validPhoneNumber("(123) 456-7890"))
		self.assertTrue(validPhoneNumber("(1111)555 2345"))
		self.assertTrue(validPhoneNumber("(098) 123 4567"))

if __name__ == '__main__':
	unittest.main()
