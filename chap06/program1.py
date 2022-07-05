import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/cannay_tset.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

(x, y), (w, h) = (180, 37), (100, 100)
roi_img = image[y:y+h, x:x+w]

arr = np.zeros((1, 255)) #1행 255열 리스트 만들기

for row in roi_img:
    for pixel in row:
        for i in range(255):
            if (i == pixel):
                arr[0][i] += 1 #해당 픽셀 값이면 배열에 1을 더함

low = 0
for i in arr[0]:
    if(i > 0):
        break
    low = low + 1

high1 = 0
for i in reversed(arr[0]):
    if(i > 0):
        break
    high1 = high1 + 1
high = 255 - high1

hist = cv2.calcHist([roi_img], [0], None, [32], [0, 256])
hist_img = draw_histo(hist)

cv2.rectangle(image, (x, y, w, h), 255, 1) #영역 표시
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
#cv2.imshow("hist_dst_img", hist_dst_img)

cv2.waitKey(0)