import numpy as np #package for arrays
import cv2 #package for opencv
import matplotlib.pyplot as plt

####with this function i can transform a bgr image to an rgb image, which is very usefull because
###cv2 is working with bgr
def bgr_to_rgb(img):
    #cv2.imshow('delphin1', img)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cv2.imshow('delphin2', img2)
    return img2

