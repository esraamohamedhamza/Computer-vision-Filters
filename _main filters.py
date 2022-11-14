#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img=cv2.imread('C:\\Users\\ALNOUR\\Downloads\\blurred (1).png',flags=cv2.IMREAD_COLOR)

kernel = np.array(
    [
        [-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1],
        [-1,-1,25,-1,-1],
        [-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1]
    ]
    ,dtype= np.float32
)
out_kernel = cv2.filter2D(img, -1, kernel=kernel)

#blur filter
blur = cv2.blur(img,(20,20))

#GaussianBlur filter
gaussian = cv2.GaussianBlur(img, (9,9), 0)

#invert filter

inv= cv2.bitwise_not(img)


#sobel filter
sobel_y= np.array(
    [
        [-1,-1,-1],
        [0,0,0],
        [1,1,1]
    ]
,np.float32
)
sobel_x= np.array(
    [
        [1,0,-1],
        [1,0,-1],
        [1,0,-1]
    ]
,np.float32
)
sobel  = sobel_y + sobel_x
sobel1 = cv2.filter2D(img,-1,sobel,borderType=cv2.BORDER_ISOLATED)

#cv2.imwrite('‪‪C:\Users\ALNOUR\Desktop_{}image.jpg'.format(b),img)

#print(out)
f,(ax0, ax1, ax2,ax3,ax4,ax5,ax6) = plt.subplots(1,7,figsize= (30,50))
ax0.imshow(img),ax0.set_title('oraginal')
ax1.imshow(kernel),ax1.set_title('kernal')
ax2.imshow(out_kernel),ax2.set_title('out_kernel')
ax3.imshow(blur),ax3.set_title('blur')
ax4.imshow(gaussian),ax4.set_title('gaussian')
ax5.imshow(inv),ax5.set_title('invert')
ax6.imshow(sobel1),ax6.set_title('sobel')


# In[ ]:




