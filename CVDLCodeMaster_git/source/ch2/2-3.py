import cv2 as cv
import sys

img=cv.imread('source/ch2/soccer.jpg') 

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

#?? BGR 컬러 영상을 명암 영상으로 변환
#?? 반으로 축소
#?? 고정 사이즈로 변환도 시도해 보자!

cv.imwrite('soccer_gray.jpg',gray)	# 영상을 파일에 저장 
cv.imwrite('soccer_gray_small.jpg',gray_small)  
    
cv.imshow('Color image',img)
cv.imshow('Gray image',gray)
cv.imshow('Gray image small',gray_small)

cv.waitKey()
cv.destroyAllWindows() 