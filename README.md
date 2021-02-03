# Cloud Coverage Index Reporter
[![Generic badge](https://img.shields.io/badge/version-3.09.10-<COLOR>.svg)](https://shields.io/)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Generic badge](https://img.shields.io/badge/contributors-2-blue)](https://shields.io/)  
[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  


## Table of contents
* [About the project](#acerca-del-proyecto)
* [How to start](#como-empezar)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [How to use](#uso)
* [Documentation](#Documentación)




# About the project
This project aims to calculate the Cloud Coverage Index according to Photographs in .JPG format with a 360 ° wide angle lens, with 4,368 pixels wide, 2,912 pixels high (center in column 2184 and line 1456) about 32MB in size. Considering that the image of the sky is a circle with an approximate radius of 1324 pixels 
```
src
```

this directory contains the executable file; in this case to run from Terminal, it is recommended 

```
python Main.py <abs route/Your image.jpeg> [s, S (optional)] [p, P (optional)]
```
Or
```
python3 src/Main.py <abs route /Your image.jpeg> [s, S (optional)] [p, P (optional)]
```



# How to start
It is necessary to mention that the project is written in Python, under versions greater than or equal to Python 3.8, therefore it is advisable to update your computer to the most recent Python version, otherwise some failures may occur, and in the same way we recommend running on computers with GNU LINUX Operating System in any of its distros.
It is also necessary to install some extra libraries, you do not need to worry about installing each one of them correctly, thanks to pip


## Prerequisites
* Verifica utilizar una versión superior a Python3.6 :
```
python --version
```
> `Python 3.8+` is adviced  

  On some Linux distros, you will run it as:  
  ```
  python3 --version
  ```


* You can check if you have PyPI installed as well as Python
   Available in the following article 
  [PyPI](https://www.tecmint.com/install-pip-in-linux/) up.  

* Have pip "Pip Installs Packages" installed to install the necessary libraries 

## How to Install
1. Clone the repository
```
git clone https://github.com/DavidHdezU/Cloud-Cover-Index-Reporter
```
2. Check the installation of the libraries with: 

  ```
  pip install -r requirements.txt
  ```
  It will install:
  * `OpenCV`
  * `NumPy`
  * `Matplot`
  * `Pdoc`
 3. After installing the libraries, please run the unit tests with this command. You will have to locate yourself in the src folder 
 ```
 cd Cloud_Coverage_Index/src/
 python3 -m pytest -v
 ```
 
# How to use

From the Cloud-Cover-Index directory:
```
python3 src/Menu.py [Image to process] [s o S (optional)] [p o P (optional)]
```

The s flag will save to a new directory called 
```
segmented_images
```
which will be in the same directory where the src / folder is located, an image with the segmentation applied to the original image with the name 
```
imageName + -seg + .JPG
```
The p flag will show you a plot to appreciate the original image
and the segmented image 

## Documentation

To generate the project documentation, the Pdoc API is used
Below are instructions on how to generate it:

1.We must put the following command in a terminal
```
export PYTHONPATH="abs-path/Cloud-Cover-Index-Reporter/Cloud_Coverage_Index/src/"
```
2. Create a new directory where to save the files that will be generated 
```
Example: mkdir docs
```
3. Run the following command in terminal 
[NOTE] Remember that to obtain the absolute path in GNU / LINUX systems you can use the command:
```
pwd
```
And for such an instance it will only be necessary to write / resources
Same case for the new directory

```
pdoc --html <ruta absoluta/Cloud-Cover-Index-Reporter/Cloud_Coverage_Index/src/> --output-dir <ruta absoluta/LaCarpetaQueCreada>

```
4. In the folder you created you will find a folder called resources, and there will be the documentation html files
5. Open index.html 


# Build by:
#### David Hernández Urióstegui & Ian Israel García Vázquez

[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=iangarcia@ciencias.unam.mx)
[<img src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/>](https://mail.google.com/mail/?view=cm&source=mailto&to=Dhdezu@ciencias.unam.mx)





---
![forthebadge biult-with-love](https://forthebadge.com/images/badges/built-with-love.svg) 
[![forthebadge powered-by-electricity](https://forthebadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)  

---
[Go up](#Cloud_Coverage_Index_Reporter)
