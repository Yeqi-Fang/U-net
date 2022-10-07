import cv2 as cv

img = cv.imread(r"D:\multi_media\pic\Feedback\{A13567C1-3A91-4428-AEFE-0CE510E8DD29}\Capture001.png")
# img2 = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
cv.imshow('thres', img)
cv.waitKey(0)
cv.destroyAllWindows()