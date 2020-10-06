import cv2

cam = cv2.VideoCapture(0)


def segment_orange_color(src_bgr):
    hsv_img = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2HSV)
    src_h = hsv_img[:, :, 0]
    src_s = hsv_img[:,:, 1]
    src_v = hsv_img[:,:, 2]

    th_min = 0
    th_max = 10
    mask_h = cv2.inRange(src_h, th_min, th_max)
    print(mask_h)

    min_sat = 0.73
    ret, mask_s = cv2.threshold(src_s,
                                min_sat * 255, 255,
                                cv2.THRESH_BINARY)

    # Combine two mask images
    mask_hs = cv2.bitwise_and(mask_h, mask_s)
    segment_img = cv2.bitwise_and(src_bgr, cv2.cvtColor(mask_hs, cv2.COLOR_GRAY2BGR))
    return segment_img


while True:
    retval, img = cam.read()

    if(retval):
        cv2.imshow("Original", img)

        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        cv2.imshow("Segment Orange", segment_orange_color(img))

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
if cam.isOpened():
    cam.release()
