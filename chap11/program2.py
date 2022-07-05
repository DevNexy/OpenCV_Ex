import numpy as np, cv2
from Common.interpolation import scaling    #interpolation 모듈의 scaling() 함수 임포트

def scaling_nearest(img, size): #크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)   #행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])   #변경 크기 비율
    i=np.arange(0, size[1], 1)  #목적 영상 세로(i) 좌표 생성
    j=np.arange(0, size[0], 1)  #목적 영상 가로(i) 좌표 새엉
    i, j = np.meshgrid(i,j)
    y,x = np.int32(i / ratioY), np.int32(j / ratioX)    #입력 영상 좌표
    dst[i, j] = img[y, x]   #역방향 사상->입력 영상 좌표 계산

    return dst

def scaling_nearest2(img, size): #크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)   # 행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2]) #변경 크기 비율
    for i in range(size[1]): # 2중포문으로 역방향 순회
        for j in range(size[0]):
            y, x = int(i / ratioY), int(j / ratioX)
            dst[i, j] = img[y, x]
    return dst

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = scaling(image, (350, 400)) #크기 변경- 기본
dst2 = scaling_nearest(image, (350, 400))   #크기 변경- 최근접 이웃 보간
dst3 = scaling_nearest2(image, (350, 400))  #크기 번경- 최근접 이웃 보간

cv2.imshow("image", image)
cv2.imshow("dst1- forward mapping", dst1)   #순방향 사상
cv2.imshow("dst2- NN interpolation", dst2)  #최근접 이웃 보간
cv2.imshow("My dst3", dst3) #역방향 이웃 보간
cv2.waitKey(0)