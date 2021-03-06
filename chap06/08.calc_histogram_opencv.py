import numpy as np, import cv2

def calc_histo(image, histSize, ranges=[0,256]):
    hist = np.zeros((histSize, 1), np.float32)
    gap = ranges[1]/ histSize

    for row in image:
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1
    return hist

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/pixel.jpg", cv2.IMREAD_GRAYSCALE) #영상 읽기
if image is None : raise Exception("영상파일 읽기 오류")

histSize, ranges = [32], [0, 256] #히스토그램 간격수, 값 범위
gap = ranges[1]/histSize[0] #계급 간격
ranges_gap = np.arange(0, ranges[1]+1, gap) #넘파이 계급범위 &간격
hist1 = calc_histo(image, histSize, ranges) #User 함수
hist2 = cv2.calcHist([image], [0], None, histSize, ranges) #OpenCV 함수
hist3, bins = np.histogram(image, ranges_gap) #numpy 모듈 함수

print("User 함수: \n", hist1.flatten()) #1차원 행렬 1행 표시
print("OpenCV 함수: \n", hist2.flatten())
print("numpy 함수: \n", hist3)