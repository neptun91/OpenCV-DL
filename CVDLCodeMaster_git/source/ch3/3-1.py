import cv2 as cv

import sys

img=cv.imread('source/ch3/soccer.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('original_RGB',img)
#?? 이미지의 왼쪽 위 1/4 만 그려보기
#?? 이미지의 정중앙 1/4 만 그려보기

#?? Red 이미지만 그려보기
#?? Green 이미지만 그려보기
#?? Blue 이미지만 그려보기

cv.waitKey()
cv.destroyAllWindows()