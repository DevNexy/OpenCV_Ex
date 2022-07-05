import numpy as np, cv2

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/median.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def maxPooling(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize//2

    for i in range(rows):
        for j in range(cols):
            y1,y2 = i - center, i + center + 1
            x1,x2 = j - center, j + center + 1
            if y1 < 0 or y2 > rows or x1 < 0 or x2> cols:
                dst[i, j] = image[i, j]
            else:
                mask = image[y1:y2, x1:x2]
                dst[i, j] = cv2.mean(mask)[0]