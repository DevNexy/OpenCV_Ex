import numpy as np, cv2

image= cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def convolution(image, mask):
        rows, cols = image.shape[:2]
        # dst = np.zeros((rows, cols), np.float32)
        ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

        dst = np.zeros((rows, cols), np.float32)

        #2차원 컨볼루션 구현
        for imageRow in range(ycenter, rows-ycenter):
                for pixel in range(xcenter, cols-xcenter):
                        sum = 0

                        for kernelRow in range(mask.shape[0]):
                                for element in range(mask.shape[1]):
                                        y,x = imageRow + kernelRow -ycenter, pixel +element -xcenter
                                        sum += image[y,x]*mask[kernelRow,element]
                        dst[imageRow, pixel] = sum
        return dst

data1 = [-1, 0, 1, #수직마스크
        -2, 0, 2,
        -1, 0, 1]
mask1 = np.array(data1, np.float32).reshape(3,3)

data2 = [-1, -2, -1, #수평마스크
        0, 0, 0,
        1, 2, 1]
mask2 = np.array(data2, np.float32).reshape(3,3)

def sqr(list): #리스트 요소끼리 제곱
        return [i*i for i in list]

data1_square = sqr(data1)
data2_square = sqr(data2)
data_sum = [x+y for x,y in zip(data1_square,data2_square)] #data1. data2 리스트 더하기

print(data_sum)
data3 = np.sqrt(data_sum) #제곱근
print(data3)
mask3 = np.array(data3, np.float32).reshape(3,3)

dst1 = convolution(image, mask1) #수직 마스크를 컨볼루션에 적용
dst2 = convolution(image, mask2) #수평 마스크를 컨볼루션에 적용
# dst3 = convolution(image, mask3) #수직+수평 마스크 컨볼루션에 적용
# sobelx = cv2.Sobel(image, cv2.CV_64F,1,0,ksize=5)
# sobely = cv2.Sobel(image, cv2.CV_64F,0,1,ksize=5)

cv2.imshow("image", image)
cv2.imshow("dst1- vertical_mask", dst1)
cv2.imshow("dst2- horizontal_mask", dst2)
# cv2.imshow("dst3", dst3)
# cv2.imshow("opencv - sobelX", sobelx)
# cv2.imshow("opencv - sobelY", sobely)
cv2.waitKey(0)
