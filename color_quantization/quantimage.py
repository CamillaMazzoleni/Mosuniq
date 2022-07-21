import numpy as np #package for arrays
from sklearn.cluster import KMeans #package for clustering
import cv2 #package for opencv
from sklearn.datasets import make_blobs

# first i am converting the image in an array of values which will be used as data in cv2.kmeans
# condition is termination criteria. As soon as each of the cluster centers moves by less than criteria.epsilon on some iteration, the algorithm stops.
# In this case the maximum number of iterations is set to 50 and epsilon = 0.10
# 10 is the number of times the algorithm is executed using different initial labellings (a good compromise)
# cv2.KMEANS_RANDOM_CENTERS select random initial centers in each attempt.
def quantimage(image,k):
    i = np.float32(image).reshape(-1,3)
    condition = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_MAX_ITER,50,0.10)
    ret,label,center = cv2.kmeans(i, k , None, condition,10,cv2.KMEANS_RANDOM_CENTERS)
    # Then Convert center to uint8
    center = np.uint8(center)
    # Replace pixel values with their center value
    final_img = center[label.flatten()]
    final_img = final_img.reshape(image.shape)
    return final_img