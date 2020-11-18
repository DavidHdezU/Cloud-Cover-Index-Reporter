
#Autor: WizardProgrammer
from PIL import Image
import matplotlib.pyplot as plt
def escala_de_grises():
    #Abrimos la Imagen
    im = Image.open("img/test_sky.jpeg")
    im.show()
    #Obtenemos sus dimensiones
    x = im.size[0]
    y = im.size[1]

    """
    im.size[0] x---------------------------->x
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    v
    y
    """


    #Creamos una nueva imagen con las dimensiones de la imagen anterior
    im2 = Image.new('RGB', (x, y))
    i = 0
    while i < x: ##Realmente es una complejidad O(n)
        j = 0
        while j < y:
            #Obtenemos el valor RGB de cada pixel
            r, g, b = im.getpixel((i,j))
            #Obtenemos su equivalente en la escala de gris
           # p = (r * 0.3 + g * 0.59 + b * 0.11) Problema convirtiendo cielo a gris
            if int(b+g)>int(g+r):#  sí existen más cian que rojos y verdes Es cielo
                p=255 ##Si lo es lo convertimos en  blanco
            else:
                p=0 # en otro caso es nube y lo hacemos 0

            #Ese valor lo convertimos a entero
            cambiado = int(p)
            pixel = tuple([cambiado, cambiado, cambiado])
            #En la nueva imagen en la posición i, j agregamos el nuevo color 
            im2.putpixel((i,j), pixel)
            j += 1
        i += 1
    #Guardamos la imagen
    im2.save('Imagen_Gris.jpeg')
    im2.show()
escala_de_grises()