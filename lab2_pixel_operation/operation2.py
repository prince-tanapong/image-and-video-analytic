import cv2


def my_filter(img):
    return cv2.add(img, (50, 100, 150, 0))


cam = cv2.VideoCapture(0)
while True:
    retval, img = cam.read()
    grey_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if(retval):
        cv2.imshow("Original", img)
        cv2.imshow("My filter Camera", my_filter(img))
        cv2.imshow("Grey scale", grey_frame)
        cv2.imshow("Grey filter", my_filter(grey_frame))
    else:
        print("Error")

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
if cam.isOpened():
    cam.release()
