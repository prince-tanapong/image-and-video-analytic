import cv2


def color_reduce(inimg, default=64):
    # solution 1
    # inimg[inimg >= 255-default] = 255
    # inimg[inimg < default] = 0

    # solution 2
    return (inimg // default) * default + (default // 2)


image_path = './lab2_pixel_operation/img/operation1_color.jpg'

img = cv2.imread(image_path)
cv2.imshow("original color", img)

post_img = color_reduce(img, 64)
cv2.imshow("posterize color", post_img)

grey_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("grey scale color", grey_img)

post_grey_img = color_reduce(grey_img)
cv2.imshow("posterize grey color", post_grey_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
