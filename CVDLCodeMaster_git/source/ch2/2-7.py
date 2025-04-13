import cv2 as cv
import sys

img=cv.imread('source/ch2/soccer.jpg') 
  
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
def draw(event,x,y,flags,param):		# 콜백 함수
    #?? 마우스 왼쪽 버튼 클릭했을 때
    #?? 빨간색 사각형을 그림
    #?? 마우스 오른쪽 버튼 클릭했을 때
    #?? 파란색 사각형을 그림
        
    cv.imshow('Drawing',img)          
    
cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

#?? Drawing 윈도우에 draw 콜백 함수 지정

while(True):		# 마우스 이벤트가 언제 발생할지 모르므로 무한 반복
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows() 
        break