import numpy as np, cv2
from Common.fft2d import fft2, ifft2, calc_spectrum, fftshift ,FFT, IFFT   #fft 관련 함수 임포트

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/smoothing.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")
cy, cx = np.divmod(image.shape, 2)[0] #행렬 중심점 구하기
mode = 3    #FFT 방법 선택

dft, spectrum = FFT(image, mode)    #FFT 수행 및 셔플링
lowpass = np.zeros(dft.shape, np.float32)   #저주파 통과 필터
highpass = np.ones(dft.shape, np.float32)   #고주파 통과 필터
cv2.circle(lowpass, (cx, cy), 30, (1,1), -1)    #2개 채널로 값 지정
cv2.circle(highpass, (cx, cy), 30, (0,0), -1)

lowpassed_dft = dft*lowpass #주파수 필터링
highpassed_dft = dft*highpass
lowpassed_img = IFFT(lowpassed_dft, image.shape, mode)  #푸리에 역변환
highpassed_img = IFFT(highpassed_dft, image.shape, mode)

cv2.imshow("image", image)
cv2.imshow("edge_remove", lowpassed_img)  #역푸리에 변환 영상
cv2.imshow("edge_detection", highpassed_img)
cv2.imshow("spectrum_img", spectrum)
cv2.imshow("lowpass_spect", calc_spectrum(lowpassed_dft))   #필터링 후 스펙트럼
cv2.imshow("highpass_spect", calc_spectrum(highpassed_dft))
cv2.waitKey(0)