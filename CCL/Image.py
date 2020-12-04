import cv2
import numpy as np

class Image:
    """
    A class that defines an Image given a file
    """
    def __init__(self, file):
        """
        Constructor that receives an URL

        Args:
            file (str): The URL of the image
        """
        self.file = cv2.imread(file)
    
    
    def change_toRGB(self):
        """
        Change the color chanel of the image to RGB

        Returns:
            Image: The image in RGB chanel
        """
        return cv2.cvtColor(self.file, cv2.COLOR_BGR2RGB)    
    def get_RowsCols(self):
        """
        Returns the dimensions of the image

        Returns:
            List: The dimensions of the image
        """
        return self.file.shape
    
    def change_toHSL(self):
        """
        Change the color chanel of the image to HLS

        Returns:
            Image: The image in HLS chanel
        """
        return cv2.cvtColor(self.file, cv2.COLOR_BGR2HLS)