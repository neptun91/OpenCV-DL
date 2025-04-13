import cv2 as cv 

img=cv.imread('source/ch4/apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#?? 허프 변환을 활용하여 apple 찾기

for i in apples[0]: 
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2)

cv.imshow('Apple detection',img)  

cv.waitKey()
cv.destroyAllWindows()