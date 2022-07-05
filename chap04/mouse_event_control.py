#다음의 마우스 이벤트 제어 프로그램을 작성하시오.
# 1. 마우스 오른쪽 클릭 시 원(클릭좌표에서 반지름 20화소)을 그린다.
# 2. 마우스 왼쪽 버튼 클릭 시 사각형(크기 30X30)을 그린다.

import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(image, (x-30, y+30), (x,y),(255,0,0),2) #파란색 사각형
        cv2.imshow(title, image)
        pt = (-1, -1) #시작 좌표 초기화

    elif event == cv2.EVENT_RBUTTONDOWN:
        pt = (x, y)
        radius = 20
        cv2.circle(image, pt, radius, (0,0,255),2) #빨간색 원
        cv2.imshow(title, image)
        pt = (-1,-1) #시작 좌표 초기화

image = np.full((300,500,3),(255,255,255),np.uint8) #흰색 배경 영상

pt = (-1,-1)    #시작 좌표 초기화
title = "Draw Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)    #마우스 콜백 함수 등록
cv2.waitKey(0)