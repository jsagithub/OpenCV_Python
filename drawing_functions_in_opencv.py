import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Opencv', (10, 500), font, 4, (255, 255, 255), 1)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
