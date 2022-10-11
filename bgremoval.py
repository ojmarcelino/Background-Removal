import cv2
from rembg import remove

image = cv2.imread('input.jpg')
new_image = remove(image)
cv2.imwrite('output.png',new_image)
