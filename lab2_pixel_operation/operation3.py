import cv2
import numpy as np

pokemon_img = cv2.imread('./lab2_pixel_operation/img/pokemon.jpg')
python_img = cv2.imread('./lab2_pixel_operation/img/python.png')
opencv_img = cv2.imread('./lab2_pixel_operation/img/opencv.png')

# create mask for opencv image
open_cv_mask = np.zeros_like(opencv_img)
condition = (opencv_img[..., 0] == 255) & (opencv_img[..., 1] == 255) & (opencv_img[..., 2] == 255)
open_cv_mask[condition] = 255

# merge opencv image
merge_poke_n_open_cv = pokemon_img.copy()
condition = (open_cv_mask[:, :, :] == 0)
merge_poke_n_open_cv[0: opencv_img.shape[0], 0: opencv_img.shape[1], :][condition] = opencv_img[condition]

# create mask for python image
python_mask = np.zeros_like(python_img)
condition = (python_img[..., 0] == 0) & (python_img[..., 1] == 0) & (python_img[..., 2] == 0)
python_mask[condition] = 255

# calculate position of python image that place in the middle of pokemon image
condition = (python_mask[:, :, :] == 0)
pokemon_middle_y = pokemon_img.shape[0] / 2
pokemon_middle_x = pokemon_img.shape[1] / 2
python_middle_y = python_img.shape[0] / 2
python_middle_x = python_img.shape[1] / 2
start_x = int(pokemon_middle_x - python_middle_x)
end_x = int(pokemon_middle_x + python_middle_x)
start_y = int(pokemon_middle_y - python_middle_y)
end_y = int(pokemon_middle_y + python_middle_y)

# create a new copy of merge image so can reduce opacity of python sign
merge_poke_n_opencv_n_python = merge_poke_n_open_cv.copy()
merge_poke_n_opencv_n_python[start_y: end_y, start_x: end_x, :][condition] = python_img[condition]
merge = cv2.addWeighted(merge_poke_n_open_cv, 0.7, merge_poke_n_opencv_n_python, 0.3, 0)

cv2.imshow('Pokemon Orignal', pokemon_img)
cv2.imshow('OpenCV Original', opencv_img)
cv2.imshow('Python Original', python_img)
cv2.imshow('OpenCV Mask', open_cv_mask)
cv2.imshow('Python Mask', python_mask)
cv2.imshow('Merge Pokemon and OpenCV', merge_poke_n_open_cv)
cv2.imshow('Final Result', merge)

cv2.waitKey(0)
cv2.destroyAllWindows()
