import cv2
###FUNCTION TO ANALYZE AN IMAGE

### SCAN
#scan an array of square and determine the avg color values for every square
#puts the value of avg r,g,b in each array
#parameter pixel= array of images (squares)
#color = array where to put the color of the image
def scan(pixel, color):
    k=0
    for i in pixel: # white balancing of image
        #print(k)
        b, g, r = cv2.split(i)
        # cv2 works with bgr so i am changing r to b to trasform it into rgb
        b_avg = cv2.mean(b)[0]
        g_avg = cv2.mean(g)[0]
        r_avg = cv2.mean(r)[0]
        #print(int(r_avg),int(g_avg),int(b_avg))
        color2 = int(b_avg), int(g_avg), int(r_avg)
        color.append(color2)
        k+=1
        

#pixel =array of images
#calculate min and max of every value
def find_min_max(pixel):
    for i in pixel: # white balancing of image
        r, g, b = cv2.split(i)
        r_avg = cv2.mean(r)[0]
        g_avg = cv2.mean(g)[0]
        b_avg = cv2.mean(b)[0]
        # cv2 works with bgr so i am changing r to b to trasform it into rgb
        b_vector.append(r_avg)
        g_vector.append(g_avg)
        r_vector.append(b_avg)
    rmin=min(r_vector)
    rmax=max(r_vector)
    gmin=min(g_vector)
    gmax=max(g_vector)
    bmin=min(b_vector)
    bmax=max(b_vector)
