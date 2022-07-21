import cv2
import numpy as np #package for arrays
#######DRAWCUBE
#drawcube is a subroutine that allows me to divide the image in subimages 
#the image is a square because we resized it
#img_size is the dimension (es 300 if image is 300x300)
#nr is number of columns/rows (es 3 if image is 3x3)
def drawCube(img, img_size, nr, start_point):
    cell_size = int(img_size / nr)
    # draw horizontal lines first
    for i in range(nr+ 1):
        start_line = (start_point[0], start_point[1] + i * cell_size)
        end_line = (start_point[0] + img_size, start_point[1] + i * cell_size)
        cv2.line(img, start_line, end_line, black, thickness)
    
    for i in range(nr + 1):
        start_line = (start_point[0] + i * cell_size, start_point[1])
        end_line = (start_point[0] + i * cell_size, start_point[1] + img_size)
        cv2.line(img, start_line, end_line, black, thickness)

    return img


####DRAW FUNCTION
###starting from a black blank image i redraw every pixel, using the colors value in colors
##h is the dimension of the image
def draw(colors,h,w):
    #Create blankimage
    blackblankimage = np.zeros(shape=[h, w, 3], dtype=np.uint8)
    k=0
    cell_size= 1
    for i in range(h):
        for j in range (w):
            cv2.rectangle(blackblankimage, pt1=(int(j*cell_size), int(i*cell_size)), pt2=(int(j*cell_size+cell_size), int(i*cell_size+cell_size)), color=(colors[k]),thickness=-1)
            k=k+1
    return blackblankimage


