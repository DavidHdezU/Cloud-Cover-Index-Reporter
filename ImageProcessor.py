import cv2
import numpy as np
from Image import Image

class ImageProcessor:
    def __init__(self, img):
        self.img = img.change_toRGB()
        self.imageHSL = img.change_toHSL()
        
    def white_mask(self):
        # Define ranges colors
        low = np.array([np.round(0/2), np.round(0.75 * 255), np.round(0.00 * 255)])
        higher = np.array([np.round(360/2), np.round(1.00 * 255), np.round(0.275 * 255)])
        
        return cv2.inRange(self.imageHSL, low, higher)
    
    def grey_mask(self):
        # Define range colors
        low = np.array([np.round(  0 / 2), np.round(0.75 * 255), np.round(0.00 * 255)])
        higher = np.array([np.round(360 / 2), np.round(1.00 * 255), np.round(0.275 * 255)])
        
        return cv2.inRange(self.imageHSL, low, higher)
    
    def white_grey_mask(self):
        binary_mask = cv2.bitwise_or(self.white_mask(), self.grey_mask())
        result = cv2.bitwise_and(self.img, self.img, mask = binary_mask)
        
        return result
            
    
    def result_image(self):
        image = self.white_grey_mask()
        rows, cols, _ = image.shape
        
        # Convert to binary
        img_binary = np.zeros((rows, cols, 1))
        
        # Need grayscale to get binary mask
        img_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        (thresh, img_binary) = cv2.threshold(img_grayscale, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        return img_binary    
    
    def __get_CircleArea(self):
        return np.pi * (1324*1324)
    
    def get_CCI(self):
        cloud_pixels = cv2.countNonZero(self.result_image())
        
        return cloud_pixels / self.__get_CircleArea()
    
            
        
        
        
        
        
        
        