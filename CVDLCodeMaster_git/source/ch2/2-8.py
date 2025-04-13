import cv2 as cv
import sys

img=cv.imread('source/ch2/girl_laughing.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
def draw(event,x,y,flags,param):
    global ix,iy
    
    #?? 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
    #??
    #?? 마우스 왼쪽 버튼 클릭했을 때 직사각형 그리기
    #??
    
    cv.imshow('Drawing',img)
    
cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

#??

while(True):
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()      
        break