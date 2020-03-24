# crop-image-python
Image cropping automation using python. Crop the same type of images as the your requirement by adding the image co-ordinates to the script. The script will take all images in the specified folder and crops according to the co-ordinates given and save the folder where you run the script in the same name. You can make changes to the script as your needs

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
````
# Setting the points for cropped image change accordingly
left = 1174
top = 2872
right = 2474
bottom = 3798
````
Here you have to set the image co-ordinates as which part you need to crop. You can find the co-ordinates of the image through GIMP or many other tools. In GIMP the co-ordinates are shown as points. It will pixel deafault you have to change it into points to see the co-ordinates
```
# saves
im1 = im1.save(x)
```
If you need to store it into a specified folder add the location in the place of 'x'
```
python crop.py
```
The last tinhg you have to do. The images will be croped and saved