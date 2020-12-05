import cv2
import numpy as np
from Image import Image

class ImageProcessor:
    """
    A class that does every method we need
    to do in order to process the image
    """
    def __init__(self, img):
        """
        Constructor that recieves an image to process

        Args:
            img (Image): Image to process
        """
        self.img = img.change_toRGB()
        self.imageHSL = img.change_toHSL()
        
    def white_mask(self):
        """
        Generates a white mask to recognize clouds

        Returns:
            Image: A white mask to recognize clouds
        """
        # Define ranges colors
        low = np.array([np.round(0/2), np.round(0.75 * 255), np.round(0.00 * 255)])
        higher = np.array([np.round(360/2), np.round(1.00 * 255), np.round(0.275 * 255)])
        
        return cv2.inRange(self.imageHSL, low, higher)
    
    def grey_mask(self):
        """
        Generates a grey mask to recognize clouds

        Returns:
            Image: A grey mask to recognize clouds
        """
        # Define range colors
        low = np.array([np.round(  0 / 2), np.round(0.75 * 255), np.round(0.00 * 255)])
        higher = np.array([np.round(360 / 2), np.round(1.00 * 255), np.round(0.275 * 255)])
        
        return cv2.inRange(self.imageHSL, low, higher)
    
    def white_grey_mask(self):
        """
        Generates a white and grey mask to recognize clouds

        Returns:
            Image: A white and grey mask to recognize clouds
        """
        binary_mask = cv2.bitwise_or(self.white_mask(), self.grey_mask())
        result = cv2.bitwise_and(self.img, self.img, mask = binary_mask)
        
        return result
            
    
    def result_image(self):
        """
        Generates a binary image, where the pixels with value equal to 1, are 
        considered as clouds

        Returns:
            Image: A binary image with the clouds recognized
        """
        image = self.white_grey_mask()
        rows, cols, _ = image.shape
        
        # Convert to binary
        img_binary = np.zeros((rows, cols, 1))
        
        # Need grayscale to get binary mask
        img_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        (_, img_binary) = cv2.threshold(img_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        return img_binary   
        
    def __get_CircleArea(self):
        """
        An auxliary method to calculate the area of the
        circle where the clouds lie

        Returns:
            float: The area of the circle where the clouds lie
        """
        return np.pi * (1324*1324)
    
    def get_cloudPixels(self):
        """
        Returns the number of pixels considered as clouds

        Returns:
            int: Number of pixels considered as clouds
        """
        return cv2.countNonZero(self.result_image())
    
    def get_CCI(self):
        """
        Calculates de CCI of the given image

        Returns:
            float: The CCI of the given image
        """        
        return self.get_cloudPixels() / self.__get_CircleArea()
    
            
        
        
        
        
        
        
        