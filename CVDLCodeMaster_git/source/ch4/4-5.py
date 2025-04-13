import skimage
import numpy as np
import cv2 as cv

img=skimage.data.coffee()
cv.imshow('Coffee image',cv.cvtColor(img,cv.COLOR_RGB2BGR))

#?? SLIC 알고리즘으로 슈퍼 화소 분할. compatness 20
#?? 분할된 슈퍼 화소 표시
sp_img1=np.uint8(sp_img1*255.0)

#?? SLIC 알고리즘으로 슈퍼 화소 분할. compatness 40
#?? 분할된 슈퍼 화소 표시
sp_img2=np.uint8(sp_img2*255.0)

cv.imshow('Super pixels (compact 20)',cv.cvtColor(sp_img1,cv.COLOR_RGB2BGR))
cv.imshow('Super pixels (compact 40)',cv.cvtColor(sp_img2,cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()