import cv2 as cv

img=cv.imread('source/ch4/soccer.jpg')	# 영상 읽기

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#?? Canny edge Tlow=50, Thigh=150으로 설정
#?? Canny edge Tlow=100, Thigh=200으로 설정

cv.imshow('Original',gray)
cv.imshow('Canny1',canny1)
cv.imshow('Canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()