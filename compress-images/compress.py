from PIL import Image 
from os import listdir
from os.path import isfile, join

# path to the directory
path = './image2/'

# list all the file names to files variable
files = [file for file in listdir(path) if isfile(join(path, file))]

# iterates with the count of files
for x in files:
 
    im = Image.open(r"./image2/"+x) 
     
    # compresses and saves here 30 is the quality it decreases from 100 to 0
    im = im.save("./compress/"+x, format="JPEG", quality=30)
    print("Compresed image "+x)

print("Compression completed")