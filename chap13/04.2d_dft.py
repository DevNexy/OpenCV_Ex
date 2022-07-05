import time

import numpy as np, cv2
from Common.dft2d import dft, idft, calc_spectrum, fftshift #dft 관련 함수 임포트

def dft2(image):
    tmp = [dft(row) for row in image]
    dst = [dft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)    #전치 환원 후 반환

def idft2(image):
    tmp = [idft(row) for row in image]
    dst = [idft(row) for row in np.transpose(tmp)]
    return np.transpose(dst)    #전체 환원 후 반환

def ck_time(mode = 0):  #수행시간 체크 함수
    global stime    #함수 내부에서 값 유지위해
    if(mode == 0):
        stime = time.perf_counter()
    elif(mode == 1):
        etime = time.perf_counter()
        print("수행시간 = %.5f sec" % (etime - stime))  #초 단위 경과 시간

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/dft_240.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

ck_time(0)  #시작 시간 체크
dft = dft2(image)   #2차원 DFT 수행
spectrum1 = calc_spectrum(dft)  #주파수 스펙트럼 영상
spectrum2 = fftshift(spectrum1) #np.fft.fftshift() 사용 가능
idft = idft2(dft).real  #2차원 IDFT 수행
ck_time(1)  #종료 시간 체크

cv2.imshow("image", image)
cv2.imshow("spectrum1", spectrum1)
cv2.imshow("spectrum2", spectrum2)
cv2.imshow("idft_img", cv2.convertScaleAbs(idft))