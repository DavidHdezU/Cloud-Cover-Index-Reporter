import cv2
import numpy as np

class Image:
    """
    A class that defines an Image given a file
    """
    def __init__(self, file):
        self.file = self.__isImage(file)
    
    def __isImage(self, file):
        img = cv2.imread(file)
        return img
    
    def change_toRGB(self):
        return cv2.cvtColor(self.file, cv2.COLOR_BGR2RGB)
    
    def change_toHSL(self):
        return cv2.cvtColor(self.file, cv2.COLOR_BGR2HLS)
    
    def change_toGrayScale(self):
        return cv2.cvtColor(self.file, cv2.COLOR_BGR2GRAY)
    
    def get_RowsCols(self):
        return self.file.shape