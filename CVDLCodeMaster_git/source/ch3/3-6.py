import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('source/ch3/mistyroad.jpg') 

#?? 명암 영상으로 변환하고 출력
plt.imshow(gray,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

#?? 히스토그램을 구해 출력
plt.plot(h,color='r',linewidth=1), plt.show()

#?? 히스토그램을 평활화하고 출력
plt.imshow(equal,cmap='gray'), plt.xticks([]), plt.yticks([]), plt.show()

#?? 히스토그램을 구해 출력
plt.plot(h,color='r',linewidth=1), plt.show()