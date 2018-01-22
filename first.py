import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mp

#img= cv2.imread('googleImgProcess.jpg', cv2.IMREAD_GRAYSCALE)
img2 = mp.imread('oprahforbes.png') #converted img to array to png

# cv2.imshow('oprah', img)
# cv2.waitkey(0)
# cv2.destroyAllWindows()

blu = img2[:,:,0]
#plt.imshow(img2, cmap='hot')
imgplot=plt.imshow(blu)
#imgplot.set_cmap('nipy_spectral')
plt.colorbar()
plt.show()
