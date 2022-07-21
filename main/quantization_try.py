#import libraries of python
import numpy as np #package for arrays
from sklearn.cluster import KMeans #package for clustering
import cv2 #package for opencv
import matplotlib.pyplot as plt #to show the images (plot)
from sklearn.datasets import make_blobs
from math import sqrt
from PIL import Image

#my libraries
from mosaic.image_processing.Basics_image import cropImage
from mosaic.image_processing.Analyse_image import scan
from mosaic.image_processing.bgr_to_rgb import bgr_to_rgb
from mosaic.image_processing.draw_functions import draw
from mosaic.image_processing.plot import show
from mosaic.import_functions.read_text import read_text
from mosaic.import_functions.save_image import save_image
from mosaic.quantization.return_name import color_name, color_nr
from mosaic.quantization.quantimage import quantimage
from mosaic.quantization.closest_color import closest_color
from mosaic.quantization.return_name import assign_color_nr

#DECLARATION OF VARIABLES NEEDED
h=50 #h=height of image
w=50 #w= width
pixel=[] #array of pixels to scan
COLOR=[] #matrix of calculated colors
AVAILABLE_COLORS= [] #matrix of available colors
COLORTABLE= [] #imported colortable with color values, colornames and colornt
color_used=[] #array of color used
STRING_COLORNR=[] #string to pass colors to the robot

####IMPORT IMAGE
img1 = cv2.imread('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\delphin_image.jpg')


####RESIZE IMAGE
img = cv2.resize(img1, (w,h), interpolation=cv2.INTER_LINEAR)
#cv2.imshow('delphin2', img)

#### READ AVAILABLE COLORS
path_colors= 'C:\\Users\\User\\Documents\\Sheffield\\Opencv\\Lists\\glassy_box_colors.txt'
read_text(path_colors, AVAILABLE_COLORS, COLORTABLE)

###ALGORITHM
cropImage(quantimage(img,5),h,w,(0,0),pixel)
scan(pixel, COLOR)

###FIND CLOSE COLORS
for i in range(len(COLOR)):
    color_used.append(closest_color(COLOR[i],AVAILABLE_COLORS))

##REDRAW IMAGES FROM EMPTY IMAGE
algorithm_image= draw(COLOR,h,w)
mosaic_image= draw(color_used,h,w)

#SAVE IMAGES TO FILES DIRECTORY
save_image(algorithm_image, 'Algorithm_image.png')
save_image(mosaic_image, 'Mosaic_real_image.png')
save_image(cv2.resize(mosaic_image, (300,300), interpolation=cv2.INTER_AREA), 'Real_image_pixeled.png')
save_image(cv2.resize(mosaic_image, (300,300)), 'Real_image_blurred.png')
##CONVERT FROM TO BGR TO RGB
#need this because cv2 works with bgr, but matplot works with rgb
img1= bgr_to_rgb(img1)
img2= bgr_to_rgb(algorithm_image)
img3= bgr_to_rgb(mosaic_image)

res = list(set(COLOR))
res2= list(set(color_used))

#make the colors i have used to a string (to later pass it with serial comunication) and print it

for i in range(len(color_used)):
    STRING_COLORNR.append(color_nr(color_used[i],COLORTABLE))

print(STRING_COLORNR)

#returns the number of colors the algorithm uses
#vs the number of colors i am using with the available colors

print("The number of colors the algorithm is using is " + str(len(res)))
print("The number of colors from available colors i am using is " + str(len(res2)))

##print the rgb values of the colors i need for the mosaic and the name
print( "The values of colors the algorithm is using is " + str(res))
print("The values of colors from available colors i am using is "+ str(res2))
print ("For this project we are using this colors: ")
for i in range(len(res2)):
    print(color_name(res2[i], COLORTABLE))

##shows the difference between initial image, algorithm image and image with available colors
show (img1,img2,img3)
