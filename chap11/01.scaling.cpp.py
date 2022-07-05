import time

import numpy as np, cv2

def scaling(img, size): #크기 변경함수1
    dst = np.zeros(size[::-1], img.dtype)   #size와 shape는 원소 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])   #비율 계산
    y = np.arange(0, img.shape[0], 1)   #입력 영상 세로(y) 좌표 생성
    x = np.arange(0, img.shape[1], 1)   #입력 영상 가로(x) 좌표 생성
    y, x = np.meshgrid(y, x)    #i,j 좌표에 대한 정방행렬 생성
    i, j = np.int32(y* ratioY), np.int32(x * ratioX)    #목적 영상 좌표
    dst[i, j] = img[y, x]   #정방향 사상->목적 영상 좌표 계산
    return dst

def scaling2(img, size):    #크기 변경 함수2
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):   #입력 영상 순회- 순방향 사상
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)     #목적 영상의 y,x 좌표
            dst[i, j] = img[y, x]
    return dst

def time_check(func, image, size, title):   #수행시간 체크 함수
    start_time = time.perf_counter()
    ret_img = func(image, size)
    elapsed =(time.perf_counter() - start_time) * 1000
    print(title, "수행시간 = %0.2f ms" % elapsed)
    return ret_img

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/scaling.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = scaling(image, (150, 200))   #크기 변경-축소
dst2 = scaling2(image, (150, 200))  #크기 변경-축소
dst3 = time_check(scaling, image, (300, 400), "[방법1]: 정방행렬 방식>")    #확대
dst4 = time_check(scaling2, image, (300, 400), "[방법2]: 반복문 방식>")    #확대

cv2.imshow("image", image)
cv2.imshow("dst1- zoom out", dst1)
cv2.imshow("dst3- zoom out", dst3)
cv2.resizeWindow("dst1- zoom out", 260, 200)    #윈도우 크기 확장
cv2.waitKey(0)