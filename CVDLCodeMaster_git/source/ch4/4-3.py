import cv2 as cv
import numpy as np

img=cv.imread('source/ch4/soccer.jpg')	 # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#?? Canny edge 찾기

#?? 모든 윤곽선을 계층 관계 없이 가져와서 저장

lcontour=[]   
for i in range(len(contour)):
    #?? 100 이상의 윤곽선을 lcontour에 연결하여 저장
    #??
    
#?? 이미지 상에 윤곽선을 그림.
             
cv.imshow('Original with contours',img)    
cv.imshow('Canny',canny)    

cv.waitKey()
cv.destroyAllWindows()