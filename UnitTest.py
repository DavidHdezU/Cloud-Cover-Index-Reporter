import unittest
from Image import Image
from ArgumentParser import ArgumentParser
import sys

class UnitTest(unittest.TestCase):
	"""
	This Unit Test Class has been developed to verify that 
	  components are working without 
	'killing the process' by omissions or errors

	"""
	def test_give_me_a_name(self):
		"""
		Verify that a wrong Argument raise an Exception
		"""
		self.assertRaises(ValueError,ArgumentParser.give_me_a_name, None)

	def test_give_me_a_name_returns(self):
		self.assertEqual(ArgumentParser.give_me_a_name("1111.JPEG"), "1111-seg.JPEG")
		self.assertNotEqual(ArgumentParser.give_me_a_name("1111.jpeg"), "1111.jpeg")
		self.assertEqual(ArgumentParser.give_me_a_name("11.11.jpeg"), "1111-seg.jpeg")













if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)
	unittest.main()

