import cv2 as cv
import sys

img=cv.imread('/Users/jinwookkwon/Dropbox/권진욱/Work/교재모음/딥러닝/컴퓨터비전과딥러닝/source_4548_1/source/ch2/girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)	# 직사각형 그리기
cv.putText(img,'laugh',(830,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)	# 글씨 쓰기

cv.imshow('Draw',img)

cv.waitKey()
cv.destroyAllWindows()