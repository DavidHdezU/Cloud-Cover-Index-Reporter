from PIL import Image

"""
Podemos leer pixel por pixel; aún no convertido a blanco  negro
"""



foto= Image.open("img/test_sky.jpeg")
datos= list(foto.getdata())


for (r,g,b) in datos:
	print(r)
