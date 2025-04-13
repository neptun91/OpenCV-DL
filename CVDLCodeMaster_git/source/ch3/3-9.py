import cv2 as cv
import numpy as np
import time

def my_cvtGray1(bgr_img):
#?? 단순 루프를 이용하여 변환하는 함수
#??
#??
#??

def my_cvtGray2(bgr_img):
#?? numpy를 이용하여 변환하는 함수
#??
#??
#??
    
img=cv.imread('source/ch3/girl_laughing.jpg') 

start=time.time()
my_cvtGray1(img)
print('My time1:',time.time()-start)

start=time.time()
my_cvtGray2(img)
print('My time2:',time.time()-start)

start=time.time()
#?? cv.cvtColor 함수를 이용하여 변환하는 함수
print('OpenCV time:',time.time()-start)