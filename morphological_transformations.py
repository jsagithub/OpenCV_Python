import cv2
from matplotlib import pylot as plt

img= cv2.imread('lena.jpg',cv2.IMREAD_GRAYSCALE)
_,mask=cv2.thresholding(img,220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.unit8)
dilation = cv2.dilate(mask, kernal)
titles =['image', 'mask','dilation']
images=[img,mask,dilation]

for i in range(3):
    plt.subplot(1,3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show
