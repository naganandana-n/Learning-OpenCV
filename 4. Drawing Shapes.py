import cv2 as cv
import numpy as np

img = cv.imread('Resources/test.jpeg')
cv.imshow('Display', img)

cv.waitKey(0)