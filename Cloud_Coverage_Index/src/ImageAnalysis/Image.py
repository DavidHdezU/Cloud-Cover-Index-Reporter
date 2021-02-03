import cv2
import numpy as np
import sys

class Image:
    """
    A class that defines an Image given a file
    """
    def __init__(self, file):
        """
        Constructor that receives a path

        Args:
            file (str): The URL of the image
        """
        self.file = cv2.imread(file)
        if self.file.shape[1] != 4368 or self.file.shape[0] !=  2912:
            print("FAILURE YOUR IMAGE HAVE NOT THE SIZE")
            sys.exit(1)
    
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