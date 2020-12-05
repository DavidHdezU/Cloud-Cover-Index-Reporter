import unittest
from Image import Image
from ArgumentParser import ArgumentParser
from ImageProcessor import ImageProcessor
from Photo import Photo
import sys

class UniTest(unittest.TestCase):
    """ 
    This Unit Test Class has beed developed to verify
    that modules are working without killing the process
    by omissions or errors
    """
    def test_give_me_a_name(self):
        """ Test to verify that Photo.give_me_a_name() raises ValueError Exception"""
        photo = Photo(None)
        self.assertRaises(ValueError, photo.give_me_a_name)
        
    def test_give_me_a_name_returns(self):
        """ Test to verify that Photo.give_me_a_name() works fine"""
        photo1 = Photo("1111.jpeg")
        self.assertEqual(photo1.give_me_a_name(), "1111-seg.jpeg")
        photo2 = Photo("1111.jpg")
        self.assertNotEqual(photo2.give_me_a_name(), "1111.jpg")
        
    def test_CCI_whiteImage(self):
        """ Test to verify that the CCI is almost equal to 1, given a white image """
        img = Image("TestComponents/white.jpg")
        processor = ImageProcessor(img)
        cci = processor.get_CCI()
        self.assertAlmostEqual(round(cci, 2), 0.99) # Because the circle in its edges has like a lighthing
        
    def test_CCI_blackImage(self):
        """ Test to verify that the CCI is equal to 0, given a black image """
        img = Image("TestComponents/black.jpg")
        processor = ImageProcessor(img)
        cci = processor.get_CCI()
        self.assertAlmostEqual(round(cci, 2), 0)
        
    
if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)
	unittest.main()