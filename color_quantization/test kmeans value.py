################
###IMPORTS#####
################
import cv2
import os
import numpy as np #package for arrays
from sklearn.cluster import KMeans #package for clustering
import cv2 #package for opencv
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from math import sqrt

################
######SETUP#####
################
h=50 #h=height=width of image
pixel=[]
COLOR=[] #array of calculated colors
AVAILABLE_COLORS= [] #array of available colors
color_used=[] #array of color used
img = cv2.imread('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\uccello.jpg')
cv2.imshow('delphin', img)

img = cv2.resize(img, (h,h), interpolation=cv2.INTER_CUBIC)
cv2.imshow('delphin2', img)

with open('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\available_colors.txt') as input_file:
    for line in input_file:
        r_available, g_available, b_available = (item.strip() for item in line.split(';', 2))
        color = int(r_available), int(g_available), int(b_available)
        #print(r_available, g_available, b_available)
        AVAILABLE_COLORS.append(color)

path = 'C:\\Users\\User\\venv_mosaic\\env2\\Scripts\\Images'
################
###FUNCTIONS#####
################

def cropImage(img, img_size, nr, start_point):
    cell_size = int(img_size / nr)
    for i in range(nr):
        for j in range (nr):
            crop= img[start_point[0]+i*cell_size:start_point[0]+i*cell_size+cell_size, start_point[1]+j*cell_size:start_point[1]+j*cell_size+cell_size]
            pixel.append(crop)

def scan(pixel):
    for i in pixel: # white balancing of image
        b, g, r = cv2.split(i)
        b_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        r_avg = cv2.mean(b)[0]
        color2= int(r_avg), int(g_avg), int(b_avg)
        COLOR.append(color2)

def closest_color(rgb):
    r, g, b =rgb
    color_diffs = []
    for color in AVAILABLE_COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    color_min = min(color_diffs)[1]
    color_used.append(color_min)
    return color_min


#def quantimage(img,k,x):
def quantimage(img, k):
    i = np.float32(img).reshape(-1,3)
    condition = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER,30,0.10)
    #condition = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER, x, 0.10)
    ret,label,center = cv2.kmeans(i, k , None, condition,10,cv2.KMEANS_RANDOM_CENTERS)
    print ("Calculating algorithm with "+ str(k)+" colors")
    # Then Convert center to uint8
    center = np.uint8(center)
    # Replace pixel values with their center value
    final_img = center[label.flatten()]
    final_img = final_img.reshape(img.shape)
    return final_img

#def draw(f,x):
def draw(f):
    blackblankimage = np.zeros(shape=[h, h, 3], dtype=np.uint8)
    blackblankimage2 = np.zeros(shape=[h, h, 3], dtype=np.uint8)
    #array_created = np.full((h, h, 3),255, dtype=np.uint8)
    k=0
    cell_size=1
    for j in range(h):
        for i in range (h):
           # cv2.rectangle(blackblankimage, pt1=(int(i*cell_size), int(j*cell_size)), pt2=(int(i*cell_size+cell_size), int(j*cell_size+cell_size)), color=(int(r_vector[k]),int(g_vector[k]),int(b_vector[k])),thickness=-1)
            cv2.rectangle(blackblankimage, pt1=(int(i * cell_size), int(j * cell_size)), pt2=(int(i * cell_size + cell_size), int(j * cell_size + cell_size)), color=(closest_color(COLOR[k])), thickness=-1)
            cv2.rectangle(blackblankimage2, pt1=(int(i * cell_size), int(j * cell_size)), pt2=(int(i * cell_size + cell_size), int(j * cell_size + cell_size)), color=(COLOR[k]), thickness=-1)
            k=k+1
    #print(np.unique(color_used))
    #cv2.imshow('With_available_colors', blackblankimage)
    print ("Saving image "+ "AV:nr:"+ str(f))
    #cv2.imshow('Algorithm', blackblankimage2)
    name= 'AVnr'+ str(f)+ '.png'
    #name = 'AVnr' + str(f) + 'iterations' + str(x) + '.png'
    cv2.imwrite(os.path.join(path , name), blackblankimage)

    #cv2.imshow('Algorithm', blackblankimage2)
    #print("Saving image " + "AL:nr:" + str(f) + "iterations:" + str(x))
    name2 = 'ALnr' + str(f) + '.png'
    #name2 = 'ALnr' + str(f) + 'iterations' + str(x) + '.png'
    cv2.imwrite(os.path.join(path ,name2), blackblankimage2)

################
#####MAIN#######
################
i_min= 3 #min number of colors i want to use
i_max=10 #max number of colors i want to use
i_values= [3,9,27,81,200]
#x_values= [10, 30, 50]
for i in i_values:
    #for x in x_values :
       #cropImage(quantimage(img,i,x),h,h,(0,0))
        cropImage(quantimage(img, i), h, h, (0, 0))
        scan(pixel)
        draw(i)