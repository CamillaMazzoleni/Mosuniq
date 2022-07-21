import cv2
import os
##i am saving the image to the files directory
###remeber thath cv2 works with bgr so save the picture before transforming it to rgb
def save_image(img,name):
    path = 'C:\\Users\\User\\venv_mosaic\\env2\\mosaic\\files'
    cv2.imwrite(os.path.join(path, name), img)