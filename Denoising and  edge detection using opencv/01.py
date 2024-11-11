# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread("../images/BSE_noisy.jpg")
kernel = np.ones((3,3), np.float32) / 9
filt_2D = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (3,3))
gaussian_blur = cv2.GaussianBlur(img, (3,3), 0)
median_blur = cv2.medianBlur(img, 3)
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)

# %%
cv2.imshow("Original Image", img)
cv2.imshow("2D custom filter", filt_2D)
cv2.imshow("2D custom filter", filt_2D)
cv2.imshow("blur filter", blur)
cv2.imshow("gaussian_blur filter", gaussian_blur)
cv2.imshow("median_blur filter", median_blur)
cv2.imshow("bilateral", bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
