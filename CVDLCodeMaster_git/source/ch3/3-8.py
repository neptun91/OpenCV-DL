import cv2 as cv

img=cv.imread('source/ch3/rose.png')
patch=img[250:350,170:270,:]

img=cv.rectangle(img,(170,250),(270,350),(255,0,0),3)
#?? INTER_NEAREST를 적용한 interpolation
#?? INTER_LINEAR를 적용한 interpolation
#?? INTER_CUBIC을 적용한 interpolation

cv.imshow('Original',img)
cv.imshow('Resize nearest',patch1) 
cv.imshow('Resize bilinear',patch2) 
cv.imshow('Resize bicubic',patch3) 

cv.waitKey()
cv.destroyAllWindows()