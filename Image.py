import cv2
import numpy as np
import sys

class Image:
    """
    A class that defines an Image given a file
    """
    def __init__(self, file):
        self.file = self.__isImage(file)
    
    def __isImage(self, file):
        """
        Verify if it is an image an return it as that
        Args:
            file: The string of the path's file
        """
        try:
            img = cv2.imread(file)
            return img
        except:
            print("Image could be locked or not exists, please check your file")
            sys.exit(1)
    
    def change_toRGB(self):
        """
        Return an Image procesed by cvtColor method of cV2

        """
        try:
            return cv2.cvtColor(self.file, cv2.COLOR_BGR2RGB)
        except:
            print("[FAILURE] Check your File or path, couldn't be analysed")
            sys.exit(1)
    
    def change_toHSL(self):
        """
        Return an Image procesed by cvtColor method of cV2
        and under HLS Process
        """
        try:
            return cv2.cvtColor(self.file, cv2.COLOR_BGR2HLS)
        except:
            print("[FAILURE] File couldn't be processed")
            sys.exit(1)
    
    def change_toGrayScale(self):
        """
        Return an Image procesed by cvtColor method of cV2
        and applied under change to GrayScale
        """
        try:
            return cv2.cvtColor(self.file, cv2.COLOR_BGR2GRAY)
        except:
            print("[FAILURE] File couldn't be procesed")
            sys.exit(1)
    
    def get_RowsCols(self):
        """
        Return Rows & Columns of image processed
        """
        return self.file.shape