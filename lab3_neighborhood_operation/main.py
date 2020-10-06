import cv2
import numpy as np

ksize = 3

cam = cv2.VideoCapture(0)


def apply_gaussian_filter(img, ksize=3):
    return cv2.GaussianBlur(original_img, (ksize, ksize), 0)


def apply_sharpen_filter(img):
    sharpen_kernel = np.zeros((3, 3), np.float32)
    sharpen_kernel.itemset((1, 1), 2)
    sharpen_kernel -= np.ones((3, 3), np.float32) / 9
    sharpen_kernel = cv2.flip(sharpen_kernel, flipCode=-1)
    sharpen_image = cv2.filter2D(img, -1, sharpen_kernel)
    return sharpen_image


def apply_edge_filter(img):
    edge_kernel = np.ones((3, 3), np.float32) * -1
    edge_kernel.itemset((1, 1), 8)
    edge_kernel = cv2.flip(edge_kernel, flipCode=-1)
    edge_image = cv2.filter2D(img, -1, edge_kernel)
    return edge_image


while True:
    retval, img = cam.read()
    high, width = img.shape[:2]

    dsize = (width // 2, high // 2)

    original_img = cv2.resize(img, dsize)
    blur_img = apply_gaussian_filter(img)
    sharpen_image = apply_sharpen_filter(original_img)
    edge_image = apply_edge_filter(original_img)

    all_img = np.vstack((np.hstack((original_img, blur_img)), np.hstack((sharpen_image, edge_image))))

    if(retval):
        cv2.imshow('Result', all_img)
    else:
        print("Error")

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
if cam.isOpened():
    cam.release()
