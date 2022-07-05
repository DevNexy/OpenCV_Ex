import numpy as np, cv2
from Common.interpolation import scaling_nearest    #최근접 이웃 보간 함수 임포트

def bilinear_value(img, pt):    #단일 화소 양선형 보간 수행 함수
    x,y = np.int32(pt)
    if x >= img.shape[1]-1: x = x-1 #영상 범위 벗어남 처리
    if y >= img.shape[0]-1: y = y-1

    P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten())    #4개 화소-관심 영역으로 접근
    ## 4개 화소 - 화소 직접 접근
    #P1 = float(img[y, x])  #최상단 화소
    #P2 = float(img[y + 0, x + 1])  #우상단 화소
    #P3 = float(img[y + 1, x + 0])  #좌하단 화소
    #P4 = float(img[y + 1, x + 1])  #우하단 화소
    
    alpha, beta = pt[1] - y, pt[0] - x  #거리 비율
    M1 = P1 + alpha * (P3 - P1) #1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)   #2차 보간
    return np.clip(P, 0, 255)   #화소값 saturation 후 반환

def scaling_bilinear(img, size):    #양선형 보간
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])   #변경 크기 비율-행태와 크기

    dst = [[bilinear_value(img, (j/ratioX, i/ratioY))   #리스트 생성
            for j in range(size[0])]
           for i in range(size[1])]
    return np.array(dst, img.dtype)

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/interpolation.jpg",cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

size = (350, 400)
dst1 = scaling_bilinear(image, size)    #크기 변경 - 양선형 보간
dst2 = scaling_nearest(image, size) #크기 변경 - 최근접 이웃 보간
dst3 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR)  #OpenCV 함수 - 양선형
dst4 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST) #OpenCV 함수 - 최근접

cv2.imshow("image", image)
cv2.imshow("User_bilinear", dst1)
cv2.imshow("User_Nearest", dst2)
cv2.imshow("OpenCV_bilinear", dst3)
cv2.imshow("OpenCV_Nearest", dst4)
cv2.waitKey(0)