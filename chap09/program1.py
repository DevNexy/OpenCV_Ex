import numpy as np, cv2
from Common.filters import filter #filters 모듈의 filter() 함수 임포트

image= cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/laplacian.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(image)
zero = np.zeros(image.shape[:2], np.uint8)

data1 = [1/9,1/9,1/9, #블러링 마스크 원소 저장
         1/9,1/9,1/9,
         1/9,1/9,1/9]
mask1 = np.array(data1, np.float32).reshape(3,3)

data2 = [0,-1,0, #1차원 리스트
         -1, 5, -1,
         0, -1,0]
mask2 = np.array(data2, np.float32).reshape(3,3)

#블러링 이미지
blur1 = filter(blue, mask1)
blur1 = blur1.astype('uint8')
blur2 = filter(green, mask1)
blur2 = blur2.astype('uint8')
blur3 = filter(red, mask1)
blur3 = blur3.astype('uint8')
list_blur = [blur1, blur2, blur3]

blur = cv2.merge(list_blur)

#샤프닝 이미지
sharpen1 = filter(blue, mask2)
sharpen1 = cv2.convertScaleAbs(sharpen1)
sharpen2 = filter(green, mask2)
sharpen2 = cv2.convertScaleAbs(sharpen2)
sharpen3 = filter(red, mask2)
sharpen3 = cv2.convertScaleAbs(sharpen3)
list_sharpen = [sharpen1, sharpen2, sharpen3]

sharpen = cv2.merge(list_sharpen)

#수직 에지 검출 이미지
gaus = cv2.GaussianBlur(image, (7, 7), 0, 0) #가우시안 마스크 적용
dst1 = cv2.Laplacian(gaus, cv2.CV_16S, 7) #라플라시안 수행

gaus1 = cv2.GaussianBlur(image, (3, 3), 0) #가우시안 블러링
gaus2 = cv2.GaussianBlur(image, (9, 9), 0)
dst2 = gaus1 - gaus2 #DoG 수행

filter2d = cv2.filter2D(image, -1, mask1)
cv2.imshow("filter2d", filter2d)

cv2.imshow("image", image)
cv2.imshow("blur", blur)
cv2.imshow("sharpen", sharpen)
cv2.imshow("dst1- LoG", dst1.astype('uint8')) #형변환 후 영상 표시
cv2.imshow("dst2- DoG", dst2)

cv2.waitKey(0)