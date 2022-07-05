import numpy as np, cv2
from Common.histogram import draw_histo #히스토그램 그리기 함수 임포트

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/equalize.jpg", cv2.IMREAD_GRAYSCALE) #영상 읽기
if image is None : raise Exception("영상파일 읽기 오류")

bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges) #히스토그램 계산

##히스토그램 누적합 계산
accum_hist = np.zeros(hist.shape[:2], np.float32)
accum_hist[0] = hist[0]
for i in range(1, hist.shape[0]):
    accum_hist[i] = accum_hist[i-1] + hist[i]

accum_hist = (accum_hist / sum(hist)) * 255 #누적합의 정규화
dst1 = [[accum_hist[val] for val in row] for row in image] #화소값 할당
dst1 = np.array(dst1, np.uint8)

##numpy 함수 및 OpenCV 룩업 테이블 사용
# accum_hist = np.cumsum(hist) #누적합 계산
# cv2.normalize(accum_hist, accum_hist, 0, 255, cv2.NORM_MINMAX) #정규화
# dst1 = cv2.LUT(image, accum_hist.astype('uint8')) #룩업 테이블로 화소값 할당

dst2 = cv2.equalizeHist(image) #OpneCV 히스토그램 평활화
hist1 = cv2.calcHist([dst1], [0], None, bins, ranges) #히스토그램 계산
hist2 = cv2.calcHist([dst1], [0], None, bins, ranges)
hist_img = draw_histo(hist)
hist_img1 = draw_histo(hist1)
hist_img2 = draw_histo(hist2)

cv2.imshow("hist image", hist_img)
cv2.imshow("user_image1", hist_img1)
cv2.imshow("OpenCV_image2", hist_img2)
cv2.imshow("image", image)
cv2.imshow("dst1_user", dst1)
cv2.imshow("dst2_Opencv", dst2)

cv2.waitKey(0)