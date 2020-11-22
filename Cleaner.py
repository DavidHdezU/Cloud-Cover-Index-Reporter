import cv2
import numpy as np
import os
import glob
from PIL import Image, ImageDraw, ImageFilter
from matplotlib import pyplot as plt


class Cleaner:
	"""
	This class Define the component to get the circle that contains
	the sky, that is really that matters for us;
	The order to get an PNG Image with just the circle is

	[1] Open the image
	[2]Crop the max square and resize it
	[3]put the Mask circle transparent
	[4]Save it
	"""

	def __init__(self, url):
		"""
		string: url , the url of the image
		"""
		self.url=str(url)
		self.img= self.convertToImage(str(url))


	def convertToImage(self,url):
		"""
		Converts the url into an Image
		Throws an exception if it is not
		Returns (obj) Image
		"""
		try:
			img=Image.open(self.url)
		except:
			print(self.url+" Is not an Image")
		return img

	def crop_center(self, crop_width, crop_height):
		"""
		Return an Image centered as a rectangle
		"""
		img_width, img_height = self.img.size
		return self.img.crop(((img_width - crop_width) // 2,(img_height - crop_height) // 2,(img_width + crop_width) // 2,(img_height + crop_height) // 2))#Parte la imagen de dos en dos para obtener el entro y hacerlo un cuadrado

	def mask_circle_solid(self, background_color, blur_radius, offset=0):
		"""
		Make a rectangle solid with a circle in the middle
		"""
		background = Image.new(self.img.mode, self.img.size, background_color)
		offset = (blur_radius*2)+offset
		mask = Image.new("L", self.img.size, 0)#Creamos una imagen de fondo negro
		draw = ImageDraw.Draw(mask)
		draw.ellipse((offset, offset, self.img.size[0] - offset, self.img.size[1] - offset), fill=255)
		mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))
		return Image.composite(self.img, background, mask)

	def crop_max_square(self):
		"""
		Return an image with the max area as a square
		"""
		return self.crop_center( min(self.img.size), min(self.img.size))

	def mask_circle_transparent(self, imgn,blur_radius, offset=0):
		"""
		Return an Image with the circle in the center and the rest of the
		picture is transparent
		"""
		offset = (blur_radius * 2)+ offset#ESte será el espacio donde se deposita la imagen que contiene al cielo
		mask = Image.new("L", imgn.size, 0)#Crea una imagen transparente
		draw = ImageDraw.Draw(mask)
		draw.ellipse((offset, offset, imgn.size[0] - offset, imgn.size[1] - offset), fill=255)#Dejamos un molde donde sabremos que tamaño tendrá nuestra imagen
		mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))#El blur nos permite hacer mas densa la imagen y lo aplicamos sobre el molde
		result = imgn.copy()#NUestra imagen es copiado
		result.putalpha(mask)#Le aplicamos el filtro
		return result #devolvemos la imagen

	def filter_image(self):
		"""
		Returns just the center of an image
		"""
		im_square= self.crop_max_square().resize((self.img.size[0],self.img.size[0] ), Image.LANCZOS)#Practicamente la estamos volviendo un cuadrado    	
		im_thumb = self.mask_circle_transparent(im_square, 50)##50 marca el punto desde donde se verá la imagen circular
		im_thumb.save("myNewCircled.png")


c = Cleaner("img/11838.jpg")
c.filter_image()


