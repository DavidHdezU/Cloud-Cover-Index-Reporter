import argparse
from ImageProcessor import ImageProcessor
from Ploter import Ploter
from Image import Image
import sys
import cv2

class ArgumentParser:
    def __init__(self):
        self.img = Image(str(sys.argv[1]))
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-s", "-S", help = "Pass the url of an image", action='store_true')
        self.parser.add_argument("--hsl", "-hsl", help = "See HSL composition", action='store_true')
        self.parser.add_argument("--rgb", "-rgb",help = "See RGB composition", action='store_true')
        self.parser.add_argument("--plot", "-p", help = "Plot the original image and the binary masked image", action='store_true')
        self.imageProcessor = ImageProcessor(self.img)
        self.ploter = Ploter(self.img)
    
    def __create_image(self):
        cv2.imwrite('image_binary.jpg', self.imageProcessor.result_image())
        
    def main(self):
        args, unknown = self.parser.parse_known_args()   
        if args.plot:
            self.ploter.show_compareImages(self.imageProcessor.result_image())
        if args.rgb:
            self.ploter.show_RGBComposition()
        if args.hsl:
            self.ploter.show_HSLComposition()
        if args.s:
            self.__create_image()
        print("Cloud Coverage Index: " + str(self.imageProcessor.get_CCI()))
            