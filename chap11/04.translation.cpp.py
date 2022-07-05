import numpy as np, cv2

def contain(p, shape):  #좌표(y,x)가 범위내 인지 검사
    return 0<=p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)    #목적 영상 생성
    for i in range(img.shape[0]):   #목적 영상 순회-역방향 사상
        for j in range(img.shape[1]):
            x,y = np.subtract((j, i), pt)   #좌표는 가로, 세로 순서
            if contain((y, x), img.shape):  #영상 범위 확인
                dst[i, j] = img[y, x]   #행렬은 행, 열 순서

    return dst

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/translate.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = translate(image, (30, 80))   #x=30, x=80 으로 평행이동
dst2 = translate(image, (-70, -50))

cv2.imshow("image", image)
cv2.imshow("dst1: transted to (30, 80)", dst1);
cv2.imshow("dst2: transted to (-70, -50)", dst2);
cv2.waitKey(0)