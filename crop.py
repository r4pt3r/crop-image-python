from PIL import Image 
from os import listdir
from os.path import isfile, join

# path to the directory
path = './images/'

# list all the file names to files variable
files = [file for file in listdir(path) if isfile(join(path, file))]

# iterates with the count of files
for x in files:
 
    im = Image.open(r"./images/"+x) 

    # Setting the points for cropped image change accordingly
    left = 1174
    top = 2872
    right = 2474
    bottom = 3798

    # crops
    im1 = im.crop((left, top, right, bottom)) 
     
    # saves
    im1 = im1.save(x)
    print("Cropped image "+x)

print("Cropping completed")
