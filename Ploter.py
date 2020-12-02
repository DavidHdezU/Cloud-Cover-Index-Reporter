import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.colors import hsv_to_rgb
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
from Image import Image

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
    
    def show_RGBComposition(self):
        """
        A function that plots the RGB composition of the image
        """
        imageRGB = self.img.change_toRGB()
        r, g, b = cv2.split(imageRGB)
        figure = plt.figure()
        axis = figure.add_subplot(1, 1, 1, projection="3d")
        pixel_colors = imageRGB.reshape((np.shape(imageRGB)[0]*np.shape(imageRGB)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()
        axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
        axis.set_xlabel("Red")
        axis.set_ylabel("Green")
        axis.set_zlabel("Blue")
        plt.show()
    
    def show_HSLComposition(self):
        """
        A function that plots the HSL composition of the image
        """
        imageHSL = self.img.change_toHSL()
        h, s, l = cv2.split(imageHSL)
        figure = plt.figure()
        axis = figure.add_subplot(1, 1, 1, projection="3d")
        pixel_colors = imageHSL.reshape((np.shape(imageHSL)[0]*np.shape(imageHSL)[1], 3))
        norm = colors.Normalize(vmin=-1.,vmax=1.)
        norm.autoscale(pixel_colors)
        pixel_colors = norm(pixel_colors).tolist()
        axis.scatter(h.flatten(), s.flatten(), l.flatten(), facecolors=pixel_colors, marker=".")
        axis.set_xlabel("Hue")
        axis.set_ylabel("Saturation")
        axis.set_zlabel("Lighting")
        plt.show()
        
        
        
        