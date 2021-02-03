from unittest import TestCase
import sys, os
import pytest
from Controller.ArgumentParser import ArgumentParser
from ImageAnalysis.Image import Image
from ImageAnalysis.ImageProcessor import ImageProcessor

class test_General(TestCase):
    """ 
    This Unit Test Class has beed developed to verify
    that modules are working without killing the process
    by omissions or errors
    """
        
    def test_create_image(self):
        """ Test to verify that Photo.give_me_a_name() works fine"""
        
        way = os.path.abspath("TestComponents/87718.JPG")
        with pytest.raises(SystemExit) as pytest_wrapped_e:
        	Image(way)
        assert pytest_wrapped_e.type == SystemExit
        
    def test_CCI_whiteImage(self):
        """ Test to verify that the CCI is almost equal to 1, given a white image """
        path = os.path.abspath("TestComponents/white.JPG")
        img = Image(path)
        processor = ImageProcessor(img)
        cci = processor.get_CCI()
        self.assertAlmostEqual(round(cci, 2), 0.99) # Because the circle in its edges has like a lighthing
        
    def test_CCI_blackImage(self):
        """ Test to verify that the CCI is equal to 0, given a black image """
        path = os.path.abspath("TestComponents/black.JPG")
        img = Image(path)
        processor = ImageProcessor(img)
        cci = processor.get_CCI()
        self.assertAlmostEqual(round(cci, 2), 0)
        
    
if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=False)
	unittest.main()