import cv2  
import os

# read an image 
# int 1  = loads colored image 
# int 0  = loads grey scale image 
# int -1 = loads image as such including alpha channel
v = 'D:\Python\AI_Projects\OpenCV\lena.jpg'
img = cv2.imread(v)
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png',img)

