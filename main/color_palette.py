from mosaic.import_functions.read_text import read_text
from mosaic.image_processing.draw_functions import draw
from math import sqrt
import cv2
from mosaic.import_functions.save_image import save_image

COLOR_PALETTE=[]
Null= []
path= 'C:\\Users\\User\\Documents\\Sheffield\\Opencv\\Lists\\glassy_box_colors.txt'
read_text(path, COLOR_PALETTE, Null)

n=len(COLOR_PALETTE)
w= int(sqrt(n))
h=w
img= draw(COLOR_PALETTE,h,w)
save_image(cv2.resize(img, (300,300), interpolation=cv2.INTER_AREA), 'Color_palette.png')