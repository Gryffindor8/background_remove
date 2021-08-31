import cv2
import numpy as np


def show_result(winname, img, wait_time):
    scale = 0.2
    disp_img = cv2.resize(img, None, fx=scale, fy=scale)
    cv2.imshow(winname, disp_img)
    cv2.waitKey(wait_time)


img = cv2.imread('C:\\Users\\user\\Desktop\\Removal_green/sk2.png')
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# define range of green color in HSV
# lower_green = np.array([70, 200, 100])
# upper_green = np.array([90, 255, 255])
upper_green = np.array([120, 220, 100])
lower_green = np.array([40, 135, 20])
# Threshold the HSV image to extract green color
mask = cv2.inRange(img, lower_green, upper_green)
mask = cv2.bitwise_not(mask)

# cv2.imwrite('mask.png', mask)
show_result('mask', mask, 0)
cv2.destroyAllWindows()
