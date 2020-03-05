import cv2
fro matplotlib import pylot as plt

img= cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show

cv2.witKey(0)
cv2.destroyAllWindows()