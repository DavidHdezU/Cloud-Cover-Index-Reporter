# Cloud Coverage Index Reporter
[![Generic badge](https://img.shields.io/badge/version-3.09.10-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-2-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  


## Table of contents
* [Acerca del proyecto](#acerca-del-proyecto)
* [Como empezar](#como-empezar)
  * [Prerequisitos](#prerequisites)
  * [Installation](#installation)
* [Uso](#uso)
* [Documentación](#Documentación)




# Acerca del proyecto
Básicamente este proyecto tiene como objetivo calcular el Índice de Cobertura Nubosa de acuerdo a Fotografías en formato .jpeg con un lente gran angular de 360°, con 4,368 pixeles de ancho, , 2,912 pixeles de alto ( centro en la columna 2184 y el reglón 1456) de alrededor de 32 MB de tamaño. Considerando que la imagen del cielo es un círculo con radio aproximado de 1324 pixeles
```
resources
```

dicha carpeta contiene el archivo ejecutable; en este caso para ejecutar desde Terminal, se recomienda 

```
python Main.py <abs route/Your image.jpeg> [s, S (optional)] [p, P (optional)]
```
O también
```
python3 resources/Main.py <abs route /Your image.jpeg> [s, S (optional)] [p, P (optional)]
```
```
Documentación
```


# Como empezar
Primero que nada, es necesario mencionar que se encuentra escrito en Python, bajo las versiones superiores o iguales a Python3.8, por ello es recomendable actualizar a la versión de Python más reciente a tu ordenador, de lo contrario podrían ocurrir algunas fallas, y  de igual manera recomendamos ejecutar en ordenadores con Sistema Operativo GNU LINUX en cualquiera de sus versiones. 
Asimismo es necesario instalar algunas bibliotecas extras, no es necesario que te preocupes por instalar de forma correcta cada una de ellas, gracias a un script de auto-instalación


## Prerequisitos
* Verifica utilizar una versión superior a Python3.6 :
```
python --version
```
> `Python 3.8+` is adviced  

  Nota, en algunos distros de Linux, lo correras como:  
  ```
  python3 --version
  ```


* Puedes revisar si tienes instalado PyPI así como Python 
  Disponible en el siguiente artículo
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

* Tener instalado pip "Pip Installs Packages" para instalar las biblotecas necesarias

## Instalación
1. Clona el repositorio
```
git clone https://github.com/DavidHdezU/Cloud-Cover-Index-Reporter
```

2. Ubicate dentro de Cloud-Cover-Index/ y verifica la instalación de los paquetes con nuestro instalador:


  ```
  bash resources/install_library.sh
  ```
  Se instalará
  * `OpenCV`
  * `NumPy`
  * `Matplot`
  * `Pdoc`
 3. Tras instalar el bash ejecutara las pruebas unitarias, deberá aparecer la leyenda
 ```
 OK
 ```
 lo cual significa que se encuentra correcto.
 Debe ser de esta manera para que pueda correr las pruebas unitarias, ya que estas hacen uso de las imagenes de las carpeta TestComponents




# Uso

Desde la Carptea Cloud-Cover-Index
```
python3 resources/Menu.py [Ruta de la Imagen a procesar] [s o S (opcional)] [p o P (opcional)]
```

La bandera s guardará una imagen en el mismo directorio 
con la segmentación aplicada a la imagen original con el nombre
```
nombreImagen + -seg + .jpg
```

La bandera p te mostrará un plot para apreciar la imagen orginal
y la imagen segmentada

## Documentación

Para generar la documentación del proyecto se usa la API Pdoc
A continuación se muestran instrucciones de como generarla

1. Primero que nada deberemos poner el siguiente comando en una terminal
```
export PYTHONPATH="Ruta-Absoulta/Cloud-Cover-Index-Reporter/resources/"
```
2. Crear una carpeta donde guardar losa archivos que se generarán
```
Ejemplo: mkdir docs
```
3. Ejecutar el siguiente comando en la terminal
[NOTE] Recuerde que para obtener la ruta absoluta en los Sistemas GNU/LINUX puede disponer del comando 
```
pwd
```
Y para tal isntancia solo hará falta escribir /resources
Mismo caso para el la Carpeta Creada

```
pdoc --html <ruta absoluta/Cloud-Cover-Index-Reporter/resources/> --output-dir <ruta absoluta/LaCarpetaQueCreada>

```
4. En la carpeta que creó encontrará una carpeta llamada resources, y ahí estarán los archivos html de la documentación
5. Abrir index.html


# Desarrollado por:
#### David Hernández Urióstegui | No. de Cuenta: 420003708   &   Ian Israel García Vázquez | No. de Cuenta: 317097364

[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=iangarcia@ciencias.unam.mx)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=Dhdezu@ciencias.unam.mx)





---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#Cloud_Coverage_Index_Reporter)
