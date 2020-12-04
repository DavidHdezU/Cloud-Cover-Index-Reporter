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
		photo = Photo(None)
		self.assertRaises(ValueError,photo.give_me_a_name)

	def test_give_me_a_name_returns(self):
		photo = Photo("1111.jpeg")
		self.assertEqual(photo.give_me_a_name(), "1111-seg.jpeg")
		photo2 = Photo("1111.jpg")
		self.assertNotEqual(photo2.give_me_a_name(), "1111.jpg")













if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)
	unittest.main()

