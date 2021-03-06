import cv2

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/pixel.jpg",cv2.IMREAD_GRAYSCALE) # 영상 읽기
if image is None: raise Exception("영상파일 읽기 오류")

(x, y), (w, h) = (180, 37), (15, 10) #좌표는 x, y
roi_img = image[y:y+h, x:x+w] #행렬 접근은 y, x

#print("[roi_img] =\n", roi_img) #행렬 원소 바로 출력 가능

print("[roi_img] =")
for row in roi_img: #원소 순회 방식 출력
    for p in row:
        print("%4d" % p, end="") #순회 원소 하나씩 출력

print()

cv2.rectangle(image, (x, y, w, h), 255, 1) #관심 영역에 사각형 표시
cv2.imshow("image", image)
cv2.waitKey(0)