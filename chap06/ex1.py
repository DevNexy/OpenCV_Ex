import numpy as np, cv2
from Common.histogram import draw_histo

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/hist_stretch.jpg", cv2.IMREAD_GRAYSCALE)
# image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 실패")

def search_value_idx(hist, bias=0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0: return idx
    return -1

def mat_access1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i, j] = ((mat[i, j]-low)/high-low) * 255

bsize, ranges = [64], [0, 256]
hist = cv2.calcHist([image], [0], None, bsize, ranges)
hist_img = draw_histo(hist)

bin_width = ranges[1]/bsize[0]
low = search_value_idx(hist, 0) * bin_width
high = search_value_idx(hist, bsize[0] - 1) * bin_width

mat_access1(image)
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)

cv2.waitKey(0)