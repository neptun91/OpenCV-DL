import cv2 as cv
import sys

img=cv.imread('/Users/jinwookkwon/Dropbox/권진욱/Work/교재모음/딥러닝/컴퓨터비전과딥러닝/CVDLCodeMaster/source/ch2/soccer.jpg')	# 영상 읽기

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image Display',img)	# 윈도우에 영상 표시

cv.waitKey()
cv.destroyAllWindows()