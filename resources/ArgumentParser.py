import argparse
from ImageProcessor import ImageProcessor
from Ploter import Ploter
from Image import Image
from Photo import Photo
import sys
import cv2

class ArgumentParser:
    """
    Class implemented to receive an define the process to
    handle the image and the exit
    """


    def __init__(self):
        """
        Receives directly from the console each argument 
        NOTE: It begins from the name of the Class that is called 
        to be interpreted as argv[0], argv[1] is for the name/path
        of the picture and  finally the parser handle the arguments (flags)
        to process the exit

        Exception: If the path doesn't exists or the Image is not a legible format
        It will end the program and notify what has happened
        """
        if len(sys.argv)<=1:
            print("[FATAL ERROR] ----You must indicate  the correct path of your image")
            sys.exit(1)
        try:
            self.img = Image(str(sys.argv[1]))
        except ValueError:
            print("Verify your Image is in *.jpg format")
            sys.exit(1)
        self.image_name = str(sys.argv[1])
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-s", "-S", help = "Pass the url of an image", action='store_true')
        self.parser.add_argument("--plot", "-p", help = "Plot the original image and the binary masked image", action='store_true')
        self.imageProcessor = ImageProcessor(self.img)
        self.ploter = Ploter(self.img)



    
    def __create_image(self):
        """
        Method that write a new Image in BW (Black & White) processed and
        before the .jpg extension, will add an -seg note in the name

        """
        photo = Photo(self.image_name)

        cv2.imwrite(photo.give_me_a_name(), self.imageProcessor.result_image())
        
    def main(self):
        """
        Process the image with the features given, as
        write the image created and the Cloud Coverage Index in 
        Standar Exit
        """
        args, _ = self.parser.parse_known_args()   
        if args.plot:
            self.ploter.show_compareImages(self.imageProcessor.result_image())
        if args.s:
            self.__create_image()
        print("Cloud Coverage Index: " + str(self.imageProcessor.get_CCI()))
            
