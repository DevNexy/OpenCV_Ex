import cv2

t_low = 25
t_high = 75
def canny_edge_camera():
    capture = cv2.VideoCapture(0)
    if capture.isOpened() == False:
        raise Exception("카메라 연결 안됨")

    while True:
        ret, image_bgr = capture.read()

        # image_bgr = cv2.GaussianBlur(image_bgr, (7,7), 1.41)
        image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        image_edge = cv2.Canny(image_gray, t_low, t_high) #캐니 엣지

        cv2.imshow("Canny_edge_camera", image_edge)

        if cv2.waitKey(20) == ord('q'):
            break

canny_edge_camera()