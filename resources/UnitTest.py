import unittest
from Image import Image
from ArgumentParser import ArgumentParser
from Photo import Photo
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
		self.assertRaises(ValueError,Photo.give_me_a_name, None)

	def test_give_me_a_name_returns(self):
		self.assertEqual(Photo.give_me_a_name("1111.JPEG"), "1111-seg.JPEG")
		self.assertNotEqual(Photo.give_me_a_name("1111.jpeg"), "1111.jpeg")













if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)
	unittest.main()

