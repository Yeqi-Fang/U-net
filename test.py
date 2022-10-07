import cv2
import numpy as np
from PIL import Image

img = cv2.imread(r"D:\multi_media\pic\Saved Pictures\fangyeqi.jpg")
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
img2 = cv2.resize(img, (128, 128))
print(img2.shape)

cv2.imshow('fads', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# b = Image.open('tensorflow/data/generated_patches/images/volumedata.tif')
