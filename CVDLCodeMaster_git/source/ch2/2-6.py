import cv2 as cv
import sys

img=cv.imread('source/ch2/girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

#?? 직사각형 그리기
#?? 글씨 쓰기

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()