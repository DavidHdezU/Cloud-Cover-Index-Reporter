class Photo:
	"""
	Class implemeted to created an approach model of a photo
	from the perspective of our requeriments
	"""
	def __init__(self, url):
		"""
        Constructor that receives the URL of an Image

		Args:
			url [str]: The URL of an Image
		"""
		self.url = url

	def give_me_a_name(self):
		"""
        Method that rewrite the name of an image; and before the extension signalized by .jpg
        add a '-seg' prefix

		Raises:
			ValueError: In case that the value of self.url is None or is not str

		Returns:
			str: The name for the new image
		"""

		image_name = str(self.url)
		ext = {"jpeg", "jpg", "png", "JPEG", "JPG", "PNG"}
		if self.url is None:
			raise ValueError

		out_name = str(image_name).split(".")

		out_string_name = ""

		for x in out_name:
			if x in ext:
				out_string_name += "-seg."
			out_string_name += x
		return out_string_name