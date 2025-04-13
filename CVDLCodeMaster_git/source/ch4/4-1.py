import cv2 as cv

img=cv.imread('source/ch4/soccer.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#?? 소벨 연산자 적용
#??

#?? 절대값을 취해 양수 영상으로 변환
#??

#?? 에지 강도 계산

cv.imshow('Original',gray)
cv.imshow('sobelx',sobel_x)
cv.imshow('sobely',sobel_y)
cv.imshow('edge strength',edge_strength)

cv.waitKey()
cv.destroyAllWindows()