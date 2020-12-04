# Climatronic 3000
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





# Acerca del proyecto
Basicamente este proyecto tiene como objetivo calcular el Índice de Cobertura Nubosa de acuerdo a Fotografías en formato .jpeg con un lente gran angular de 360°, con 4,368 pixeles de ancho, , 2,912 pixeles de alto ( centro en la columna 2184 y el reglón 1456) de alrededor de 32 MB de tamaño. Considerando que la iamgen del cielo es un círculo con radio aproximado de 1324 pixeles
```
resources
```

dicha carpeta contiene el archivo ejecutable; en este caso para ejecutar desde Terminal, se recomienda 

```
python resources/Main.py <Your image.jpeg> [-s, -S (optional)]
```
```
Documentacion
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


* Tu puedes revisar si tu tienes instalado PyPI así como Python 
  Disponible en el siguiente artículo
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

## Instalación
1. Clona el repositorio
```
git clone https://github.com/DavidHdezU/Cloud-Cover-Index-Reporter
```
3. Ubicate en Tarea01/src y verifica la instalación de los paquetes con nuestro instalador:
  ```
  bash install_librarys.sh
  ```
  Se instalará
  * `gTTS`
  * `playsound`
  * `pandas`
  * `keyboard`
  * `googletrans`
 4. Tras instalar el bash ejecutara las pruebas unitarias, deberá aparecer la leyenda
 ```
 OK
 ```
 lo cual significa que se encuentra correcto




# Uso

Solo ubicarte en el directorio Tarea01/src/ deberás ejecutar
```
bash launcher.sh
```
ó 
```
python3 Menu.py
```


# Desarrollado por:
#### David Hernández Urióstegui | No. de Cuenta: 420003708   &   Ian Israel García Vázquez | No. de Cuenta: 317097364

[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=iangarcia@ciencias.unam.mx)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=Dhdezu@ciencias.unam.mx)





---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#climatronic-3000)
