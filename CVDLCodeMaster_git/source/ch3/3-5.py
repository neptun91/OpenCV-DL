import cv2 as cv
import numpy as np

img=cv.imread('source/ch3/soccer.jpg') 
img=cv.resize(img,dsize=(0,0),fx=0.25,fy=0.25)

#?? gamma값 계산하는 함수
#??
#??
#??

#?? 감마 변환하여 hstack에 저장
cv.imshow('gamma',gc)

cv.waitKey()
cv.destroyAllWindows()