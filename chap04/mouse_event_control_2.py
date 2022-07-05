# 위 과제 문제에 다음을 추가하여 프로그램을 작성하시오.
# 1. 트랙바를 추가해서 선의 굵기를 1~10픽셀로 조절한다.
# 2. 트랙바를 추가해서 원의 반지름을 1~50픽셀로 조절한다.

import numpy as np
import cv2

def onChangeLineSize(value):
    global line_size

    line_size = value

def onChangeRadius(value):
    global radius

    radius = value

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x + 30, y +30),(255,0,0), line_size) #파란색 사각형
        cv2.imshow(title, image)

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image, (x,y), radius, (0,0,255), 2) #빨간색 원
        cv2.imshow(title, image)

image = np.full((300,500,3),(255,255,255),np.uint8) #흰색 배경 영상

title = "Draw Event"
cv2.imshow(title, image)
line_size =1
radius =1
cv2.createTrackbar('line', title, line_size, 10, onChangeLineSize)
cv2.createTrackbar('radius', title, radius, 50, onChangeRadius)
cv2.setMouseCallback(title, onMouse)    #마우스 콜백 함수 등록
cv2.waitKey(0)