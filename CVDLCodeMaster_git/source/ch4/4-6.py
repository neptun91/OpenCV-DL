import skimage
import numpy as np
import cv2 as cv
import time

coffee=skimage.data.coffee()

start=time.time()
#?? SLIC 활용하여 Super pixel 생성
#?? Super pixel 간 평균 색상 유사도 기반 그래프 생성
#?? 정규화 절단 이용하여 영역 나눔
print(coffee.shape,' Coffee 영상을 분할하는데 ',time.time()-start,'초 소요')

#?? 경계선 표시
ncut_coffee=np.uint8(marking*255.0)

cv.imshow('Normalized cut',cv.cvtColor(ncut_coffee,cv.COLOR_RGB2BGR))  

cv.waitKey(0)
cv.destroyAllWindows()