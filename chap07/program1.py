import numpy as np, cv2
from Common.histogram import draw_histo #히스토그램 그리기 함수 임포트

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/equalize.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

bin, ranges =[256], [0,256]

#히스토그램 계산
hist = np.zeros(bin, np.int32)
for row in image:
    for pix in row:
        hist[pix//(ranges[1]//bin[0])]+=1

#히스토그램 누적합 계산
cum = np.zeros(hist.shape[:2], np.float32)

cum[0] = hist[0]
for i in range(1, hist.shape[0]):
    cum[i] = cum[i-1] + hist[i]
cum = (cum / sum(hist))*255
# cumulativeSum = np.array(cumulativeSum, np.uint8)

histo_equal = np.zeros(image.shape, np.float32)
for w in range(histo_equal.shape[0]): #누적합 정규화
    for h in range(histo_equal.shape[1]): #화소값 할당
        histo_equal[w, h] = cum[image[w,h]]

histo_equal = np.array(histo_equal, np.uint8)
print(histo_equal)

dst = draw_histo(cum)
dst2 = draw_histo(hist)

cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.imshow("histo_equal", histo_equal)
cv2.waitKey(0)