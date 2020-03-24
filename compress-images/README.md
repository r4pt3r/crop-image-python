# Compress Images
This script is to compress a large number of images in a folder. We can set the value of compression it compress accordingly and saves to a new folder with the same image name.

# Requirements
* python
* python pip
* pillow library

# How to use
Install python and pillow library using python pip
````
# path to the directory
path = './images/'
````
This path refers to the folder where you image files are located. Change it according to you
```
im = im.save("./compress/"+x, format="JPEG", quality=30)
```
In this part compression and saving occurs you have to set the quality. Here 30 is given as the quality. Quality and size will decreases from 100 to 0.