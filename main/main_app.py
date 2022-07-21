########IMPORTS
import numpy as np #package for arrays
from sklearn.cluster import KMeans #package for clustering
import cv2 #package for opencv
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from math import sqrt
from mosaic.image_processing.Basics_image import cropImage
from mosaic.image_processing.Analyse_image import scan
from mosaic.image_processing.bgr_to_rgb import bgr_to_rgb
from mosaic.image_processing.plot import show
from mosaic.image_processing.draw_functions import draw
from mosaic.import_functions.read_text import read_text
from mosaic.quantization.return_name import color_name, color_nr
from mosaic.quantization.quantimage import quantimage
from mosaic.quantization.closest_color import closest_color

#######VARIABLES
AVAILABLE_COLORS= [] #array of available colors
COLORTABLE=[] #imported colortable with color values, colornames and colornt
pixel=[]
COLOR=[] #array of calculated colors
color_used=[] #array of color used
STRING_COLORNR=""

####IMPORT IMAGE
path_image= 'C:\\Users\\User\\Documents\\Sheffield\\Opencv\\'
image_name= input ("Insert the name of the image you want to use for your mosaic: ")
img1 = cv2.imread(path_image+image_name)

#####DEFINE DIMENSION
h= int(input("How many columns/rows do you want to use for your mosaic? "))
img = cv2.resize(img1, (h,h), interpolation=cv2.INTER_CUBIC)

#####IMPORT LIST OF AVAILABLE COLORS
path_colorstext= 'C:\\Users\\User\\Documents\\Sheffield\\Opencv\\Lists\\'

inp = input("Do you want to use the list of available colors? y/n ")
if(inp=='y'):
    file_name='available_colors.txt'
elif inp=='n':
    file_name=input("Insert the list name: ")

###import data
read_text(path_colorstext+file_name, AVAILABLE_COLORS, COLORTABLE)

#####NUMBER OF COLORS TO USE
n= int(input("How many colors (MAXIMUM) do you want to use? "))


###MAIN
###ALGORITHM
cropImage(quantimage(img,n),h,h,(0,0), pixel)
scan(pixel, COLOR)

###FIND CLOSE COLORS
for i in range(len(COLOR)):
    color_used.append(closest_color(COLOR[i],AVAILABLE_COLORS))

##REDRAW IMAGES FROM EMPTY IMAGE
mosaic_image= draw(color_used,h)
algorithm_image= draw(COLOR,h)

for j in range(len(color_used)):
    STRING_COLORNR+=(color_nr(color_used[j], COLORTABLE)+";")
res = list(set(color_used))

print ("For this project we are using this colors: ")
for i in range(len(res)):
    print(color_name(res[i], COLORTABLE))

##CONVERT FROM TO BGR TO RGB
#need this because cv2 works with bgr, but matplot works with rgb
img1= bgr_to_rgb(img1)
img2= bgr_to_rgb(algorithm_image)
img3= bgr_to_rgb(mosaic_image)

##shows the difference between initial image, algorithm image and image with available colors
show(img1, img2, img3)
