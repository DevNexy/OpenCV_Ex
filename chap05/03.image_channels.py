import cv2

image = cv2.imread("C:/Users/we726/PycharmProjects/pythonProject/source/images/color.jpg", cv2.IMREAD_COLOR) #영상 읽기
if image is None: raise Exception("영상파일 읽기 오류") #예외 처리
if image.ndim != 3 : raise Exception("컬러 영상 아님") #예외 처리 - 컬러 영상 확인

bgr = cv2.split(image) #채널 분리 컬러 영상 -> 3채널 분리
#blue, green, red = cv2.split(image) #3개 변수로 반환받기 가능
print("bgr 자료형:",type(bgr), type(bgr[0]), type(bgr[0][0][0]))
print("bgr 원소개수:", len(bgr))

## 각 채널을 윈도우에 띄우기
cv2.imshow("image", image)
cv2.imshow("Blue channel", bgr[0]) #Blue 채널
cv2.imshow("Green channel", bgr[1]) #Green 채널
cv2.imshow("Red channel", bgr[2]) #Red 채널
#cv2.imshow("Blue channel", image[:,:,0]) #넘파이 객체 인덱싱 방식
#cv2.imshow("Green channel", image[:,:,1])
#cv2.imshow("Red channel", image[:,:,2])
cv2.waitKey(0)