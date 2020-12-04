from ImageProcessor import ImageProcessor
from Ploter import Ploter
from Image import Image
import sys
import cv2

class Photo:
	"""
	Class implemeted to created an approach model of a photo
	from the perspective of our requeriments
	"""

	def __init__(self, url:str):
		"""
		Constructor of a new Image 
		"""
		self.url=url

	def give_me_a_name(self)->str:
		"""
        Method that rewrite the name of an image; and before the extension signalized by .jpg
        add a '-seg' prefix
        Return:
            str ->New Name
        """

		image_name=str(self.url)
		ext={"jpeg", "jpg", "png", "JPEG", "JPG", "PNG"}
		if self.url is None:
			raise ValueError

		out_name=str(image_name).split(".")

		out_string_name=""

		for x in out_name:
			if x in ext:
				out_string_name+="-seg."
			out_string_name+=x
		return out_string_name
