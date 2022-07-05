import numpy as np, cv2

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/sum_test.jpg",cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류 발생")

image[60:160, 20:120] += 50
image[180:280, 150:250] += 255

cv2.imshow('image', image)
# cv2.imshow('m_add', m_add)
cv2.waitKey(0)