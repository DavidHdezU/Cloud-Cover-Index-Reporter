
#Autor: WizardProgrammer
from PIL import Image
import matplotlib.pyplot as plt
from Cleaner import Cleaner 

"""
Convierte la imagen a blanco(cielo) y negro
"""
def __init__(self, url):
    self.url=url

def is_in_circle(x,y):
    diferencia_xmenor=2184-1324
    diferencia_ymenor=1456-1324
    diferencia_xmayor=2184+1324
    diferencia_ymayor=1456+1324
    if x>=diferencia_xmenor and y>=diferencia_ymenor:
        return True
    elif x>=diferencia_xmayor and y>=diferencia_ymayor:
        return True
    return False


def escala_de_grises():
    c = Cleaner("img/11838.jpg")
    c.filter_image()
    #Abrimos la Imagen
    im = Image.open("myNewCircled.png")
    im= im.convert('RGB')
    #im.show()
    #Obtenemos sus dimensiones
    x = im.size[0]
    y = im.size[1]
    print(x,y)
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
    while i < x: # leemos pixel por pixel de la imagen Realmente es una complejidad O(n)
        j = 0
        while j < y:#Radio +centro en y

            #Obtenemos el valor RGB de cada pixel
            r,g,b = im.getpixel((i,j))#Obtenemos el pixel desde las coordenada i,j

            #Obtenemos su equivalente en la escala de gris
            if b+g>=r+g:
                p=0
                cambiado = int(p)

            else:
                p=255
                cambiado= int(p)
            pixel = tuple([cambiado, cambiado, cambiado])
            #Ese valor lo convertimos a entero
            
            
            #En la nueva imagen en la posición i, j agregamos el nuevo color 
            im2.putpixel((i,j), pixel)
            j += 1
        i += 1
    #Guardamos la imagen
    im2.save('Imagen_Gris.png')
    ##extrujamos la imagen de nuevo
    cleaner= Cleaner("Imagen_Gris.png")
    cleaner.filter_image()

    #im2.show()
escala_de_grises()