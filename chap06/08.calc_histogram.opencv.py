import numpy as np

def calc_histo(image, histSize, ranges=[0,256]): #행렬 원소의 1차원 히스토그램 계산
    hist = np.zeros((histSize, 1), np.float32) #히스토그램 누적 행렬
    gap = ranges[1]/ histSize #계급 간격

    for row in image: #2차원 행렬 순회 방식
        for pix in row:
            idx = int(pix/gap)
            hist[idx] += 1
    return hist