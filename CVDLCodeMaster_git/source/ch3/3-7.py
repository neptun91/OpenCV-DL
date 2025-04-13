import cv2 as cv
import numpy as np

img=cv.imread('source/ch3/soccer.jpg')
img=cv.resize(img,dsize=(0,0),fx=0.4,fy=0.4)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.putText(gray,'soccer',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv.imshow('Original',gray)

#?? 댜양한 값으로 가우시안 블러링을 수행
cv.imshow('Smooth',smooth)

femboss=np.array([[-1.0, 0.0, 0.0],
                  [ 0.0, 0.0, 0.0],
                  [ 0.0, 0.0, 1.0]])

gray16=np.int16(gray)
#?? 예외처리가 완료된 Embossing 수행
#?? 레벨값 제한이 없는 Embossing 수행
#?? 음수를 고려하지 않는 Embossing 수행

cv.imshow('Emboss',emboss)
cv.imshow('Emboss_bad',emboss_bad)
cv.imshow('Emboss_worse',emboss_worse)

cv.waitKey()
cv.destroyAllWindows()