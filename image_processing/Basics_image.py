import cv2
###USEFULL FUNCTIONS
### import images
### resize image
### show modified images
### crop images in squares

####IMPORT AN IMAGE
#img = cv2.imread('C:\\Users\\User\\Documents\\Sheffield\\Opencv\\green.jpg')

####SHOW AN IMAGE
#cv2.imshow('Green', img)

###RESIZE AN IMAGE
#parameters are
#img= image to resize
#(,)= height and width
#img = cv2.resize(img, (300,300), interpolation=cv.INTER_CUBIC)

###CREATE BLACK BLANK IMAGE
#blackblankimage = np.zeros(shape=[300, 300, 3], dtype=np.uint8)

####CROP AN IMAGE
#function to crop an image to squares (tiles)
#i put every square to an array
#parameters are
#img= image to modify
#img_size= dimension: in this case we assume that height = width
#nr= nr of columns/ rows to crop the image
#start point= point to start from (usually 0) (x,y)--> first value for offset on x, second for offset on y
#pixel is array of cropped images
def cropImage(img, h, w, start_point,pixel):
    k=0
    cell_size = 1
    for i in range(h):
        for j in range (w):
            crop= img[start_point[0]+i*cell_size:start_point[0]+i*cell_size+cell_size, start_point[1]+j*cell_size:start_point[1]+j*cell_size+cell_size]
            pixel.append(crop)






