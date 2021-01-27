import argparse
from ImageProcessor import ImageProcessor
from Ploter import Ploter
from Image import Image
from Photo import Photo
import sys
import cv2
import os.path

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
        if len(sys.argv) <= 1:
            print("Usó  python resources/Main.py <route/Image.jpeg>  [s (optional)] [S (optiona)] [p (optional)] [P optional]")
            sys.exit(1)
            
        if not os.path.exists(str(sys.argv[1])) or not os.path.isfile(str(sys.argv[1])):
            print(str(sys.argv[1]) + " is not a file or does not exist")
            sys.exit(1)
        try:
            self.img = Image(str(sys.argv[1]))
        except ValueError:
            print("Verify your Image is in *.jpg format")
            sys.exit(1)
        self.image_name = str(sys.argv[1])
        self.imageProcessor = ImageProcessor(self.img)
        self.ploter = Ploter(self.img)



    
    def __create_image(self):
        """
        Method that write a new Image in BW (Black & White) processed and
        before the .jpg extension, will add an -seg note in the name

        """
        photo = Photo(self.image_name)

        cv2.imwrite(photo.give_me_a_name(), self.imageProcessor.result_image())
    
    def __use(self):
        """
        Function that shows how to use the programm
        """
        print("To use this programm you need to pass as first parameter a valid image\n" +
              "You can also pass the flags 's' or 'p' \n" +
              "The flag s is to saves the segmeted image use to calculate the CCI\n" + 
              "The flag p is to plot the original image and the segmented image, to apreciate the differences\n")
        
    def main(self):
        """
        Process the image with the features given, as
        write the image created and the Cloud Coverage Index in 
        Standar Exit
        """
        if len(sys.argv) > 2:
            for i in range(2, len(sys.argv)):
                if sys.argv[i].lower() == "p":
                    self.ploter.show_compareImages(self.imageProcessor.result_image())
                elif sys.argv[i].lower() == "s":
                    self.__create_image()
                else:
                    print("This flag is unknown\n\n")
                    self.__use()
                    
        print("Cloud Coverage Index: " + str(self.imageProcessor.get_CCI()))
            
