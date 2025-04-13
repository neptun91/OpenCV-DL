import matplotlib
matplotlib.use('TkAgg')
import cv2 as cv
import sys

img=cv.imread('source/ch3/soccer.jpg') 
            
#?? 오츄 알고리즘으로 최적값과 이진화 된 영상 찾기
print('오츄 알고리즘이 찾은 최적 임곗값=',t)

cv.imshow('R channel',img[:,:,2])			# R 채널 영상
cv.imshow('R channel binarization',bin_img)	# R 채널 이진화 영상

cv.waitKey()
cv.destroyAllWindows()