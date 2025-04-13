import cv2 as cv
import numpy as np

# 1. 빈 배경 이미지 생성 (검정 배경)
img = np.zeros((300, 300, 3), dtype=np.uint8)

# 2. 원본 사각형 그리기 (파란색)
start_point = (100, 100)
end_point = (200, 200)
cv.rectangle(img, start_point, end_point, (255, 0, 0), -1)

# 3. 이동 행렬 정의 (이동: (2, -1) => 픽셀 단위로는 (20, -10))
# Note: OpenCV는 (x, y) 순서이므로, y 방향이 아래로 양수입니다.
dx, dy = 20, -10
T = np.float32([[1, 0, dx],
                [0, 1, dy]])

#?? 4. 이동 적용

#?? 5. 회전 행렬 정의 (회전 중심: 이미지 중심, 각도: 30도)

#?? 6. 회전 적용

# 7. 결과 출력
cv.imshow('Original', img)
cv.imshow('Translated (2, -1)', translated_img)
cv.imshow('Rotated 30 deg', rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()