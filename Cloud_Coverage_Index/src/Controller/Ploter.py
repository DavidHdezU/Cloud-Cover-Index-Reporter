import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.colors import hsv_to_rgb
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
from ImageAnalysis.Image import Image

class Ploter:
    """
    A class that plots the RGB and HSL 
    composition of a given image
    """
    def __init__(self, img):
        """
        Constructor that recieves an image

        Args:
            img [Image]: the image to work with
        """
        self.img = img
    
    def show_compareImages(self, result):
        """
        A function that plots the original image
        and the image with the binary mask, to see the
        differences

        Args:
            result (Image): The image with the binary mask
        """
        plt.subplot(1, 2, 1)
        plt.imshow(self.img.change_toRGB())
        plt.subplot(1, 2, 2)
        plt.imshow(result)
        plt.show()
        
        
        