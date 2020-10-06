import cv2
from matplotlib import pyplot as plt
import numpy as np

image_path = './lab4_grey_scale_segmentation/img/mandm.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

img_colormap = cv2.applyColorMap(img, cv2.COLORMAP_JET)
cv2.imshow("GRAY: ORIGINAL", img)
cv2.imshow("GRAY: ORIGINAL+COLORMAP", img_colormap)

lower = 100
upper = 145
thresh_img = cv2.inRange(img, lower, upper)
cv2.imshow("Mask:", thresh_img)

thresh_img2 = (img > lower) & (img < upper)
thresh_img2 = thresh_img2.astype(np.uint8)
thresh_img2 = thresh_img2 * 255
cv2.imshow("Mask2 :", thresh_img2)


plt.imshow(img, cmap='jet')
plt.clim(vmin=0, vmax=255)
plt.colorbar()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
