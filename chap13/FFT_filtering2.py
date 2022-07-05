import numpy as np, cv2
from Common.fft2d import FFT, IFFT, calc_spectrum   #2차원 푸리에 변환 함수 임포트
import matplotlib.pyplot as plt #그래프 그리기 임포트
from mpl_toolkits.mplot3d import Axes3D #3차원 그래프 라이브러리 임포트

def get_gaussianFilter(shape, R):   #가우시안 필터 생성 함수
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)   #x축 범위 및 간격 지정
    x = np.arange(-u[1], u[1], 1)   #y축 범위 및 간격 지정
    x, y = np.meshgrid(x, y)    #x,y 좌표 정방행렬 생성
    filter = np.exp(-(x**2+y**2)/(2*R**2))
    return x,y,filter if len(shape) < 3 else cv2.merge([filter, filter])

def get_butterworthFilter(shape, R, n): #버터워스 필터 생성 함수
    u = np.array(shape)//2
    y = np.arange(-u[0], u[0], 1)
    x = np.arange(-u[1], u[1], 1)
    x, y = np.meshgrid(x, y)
    dist = np.sqrt(x**2 + y**2)
    filter = 1/(1 + np.power(dist / R, 2 *n))
    return x, y, filter if len(shape) < 3 else cv2.merge([filter, filter])

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/filter.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

mode = 2
dft, spectrum = FFT(image, mode)    #FFT 수행 및 셔플링
x1, y1, gauss_filter = get_gaussianFilter(dft.shape, 30)    #필터 생성
x2, y2, butter_filter = get_butterworthFilter(dft.shape, 30, 10)

filtered_dft1 = dft * gauss_filter  #주파수 공간 필터링- 원소 간 곱셈
filtered_dft2 = dft * butter_filter
gauss_img = IFFT(filtered_dft1, image.shape, mode)  #역푸리에 변환
butter_img = IFFT(filtered_dft2, image.shape, mode) 
spectrum1 = calc_spectrum(filtered_dft1)    #필터링 후, 주파수 스펙트럼 영상
spectrum2 = calc_spectrum(filtered_dft2)

if mode == 3:   #OpenCV 함수는 2채널 사용하기에
    gauss_filter, butter_filter = gauss_filter[:, :, 0], butter_filter[:, :, 0]

plt.figure(figsize=(10,10)) #그래프 생성
ax1 = plt.subplot(332, projection='3d') #3차원 그래프
ax1.plot_surface(x1, y1, gauss_filter, cmap='RdPu'), plt.title("gauss_filter")
ax2 = plt.subplot(333, projection='3d')
ax2.plot_surface(x2, y2, butter_filter, cmap='RdPu'), plt.title("butter_filter")

titles = ["input image", "butter_lowpassed_image", "gauss_lowpassed_image",
          "input spectrum", "gauss_lowpassed_spectrum","butter_lowpassed_spectrum"]
images = [image, butter_img, gauss_img, spectrum, spectrum1, spectrum2] #결과 영상 행렬
plt.gray()  #명암도 영상으로 표시
for i, t in enumerate(titles):
    plt.subplot(3,3,i+4), plt.imshow(images[i]), plt.title(t)
plt.tight_layout(), plt.show()