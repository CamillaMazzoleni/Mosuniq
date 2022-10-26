#import libraries of python
import numpy as np #package for arrays
from sklearn.cluster import KMeans #package for clustering
import cv2 #package for opencv
import matplotlib.pyplot as plt #to show the images (plot)
from sklearn.datasets import make_blobs
from math import sqrt
from PIL import Image
import serial
import time

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
from mosaic.import_functions.create_list import new_list
from mosaic.arduino_comm.ComPyArd import Arduino_read, Arduino_write_pos, Arduino_comunicate


#arduino comunication
arduino_port = serial.Serial('COM3', 9600)
time.sleep(2)

#DECLARATION OF VARIABLES NEEDED
h=5 #h=height of image
w=5 #w= width
nr_colors=1 #number of colors
pixel=[] #array of pixels to scan
COLOR=[] #matrix of calculated colors
AVAILABLE_COLORS= [] #matrix of available colors
COLORTABLE= [] #imported colortable with color values, colornames and colornt
color_used=[] #array of color used
COLORTABLE2=[] #string to pass colors to the robot
ArduinoColor="";

####IMPORT IMAGE
#img1 = cv2.imread('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\delphin_image.jpg')
img1 = cv2.imread('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\brown.png')

####RESIZE IMAGE
img = cv2.resize(img1, (w,h), interpolation=cv2.INTER_LINEAR)
#cv2.imshow('delphin2', img)

#### READ AVAILABLE COLORS
path_colors= 'C:\\Users\\User\\Documents\\Sheffield\\Opencv\\Lists\\glassy_box_colors.txt'
read_text(path_colors, AVAILABLE_COLORS, COLORTABLE)
cropImage(quantimage(img,nr_colors),h,w,(0,0),pixel)
scan(pixel, COLOR)

###FIND CLOSE COLORS
for i in range(len(COLOR)):
    color_used.append(closest_color(COLOR[i],AVAILABLE_COLORS))

##REDRAW IMAGES FROM EMPTY IMAGE
algorithm_image= draw(COLOR,h,w)
mosaic_image= draw(color_used,h,w)

##CONVERT FROM TO BGR TO RGB
#need this because cv2 works with bgr, but matplot works with rgb
img1= bgr_to_rgb(img1)
img2= bgr_to_rgb(algorithm_image)
img3= bgr_to_rgb(mosaic_image)

res = list(set(COLOR))
res2= list(set(color_used))

print(res2)

COLORTABLE2=new_list(res2, COLORTABLE)

for i in range(len(color_used)):
    ArduinoColor+=(str(color_nr(color_used[i], COLORTABLE2)))
    ArduinoColor+=";";

print(COLORTABLE2)
print(ArduinoColor)

Arduino_comunicate(arduino_port, 0, color_used, COLORTABLE2)
