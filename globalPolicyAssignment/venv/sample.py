import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
The method is as follows: generate edge represontation of image -> calculate growth rate 

Orignally I was planning on using a CNN but I prefer this solution for its simplistiy.
This method uses a faction of computational power and can generate a meaningful result.
'''
#importing images, 0 gives GRAYSCALE
path = "venv/"
img_1939GS = cv2.imread(path+'Fig1_1939.jpeg',0)
img_2019GS = cv2.imread(path+'Fig2_2019.jpeg',0)
#develop edge b/w images
edges_1939 = cv2.Canny(img_1939GS,100,200)
edges_2019 = cv2.Canny(img_2019GS,100,200)
plt.subplot(221),plt.imshow(img_1939GS,cmap = 'gray')
plt.title('Original Image 1939'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_2019GS,cmap = 'gray')
plt.title('Original Image 2019'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(edges_1939,cmap = 'gray')
plt.title('Edge Image 1939'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(edges_2019,cmap = 'gray')
plt.title('Edge Image 2019'), plt.xticks([]), plt.yticks([])
plt.show()
#when viewed on a plot the 1939 image appears to be patched together
#this causes some additional generatored edges decreasing the expected result
#this method would work better on modern images
white_pix_1939 = np.sum(edges_1939 == 255)
white_pix_2019 = np.sum(edges_2019 == 255)
print('Develpment growth over 80 years:', (white_pix_2019-white_pix_1939)/white_pix_1939)