# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%

img = cv2.imread("../images/BSE_Google_noisy.jpg", 0)
median = cv2.medianBlur(img, 5)
# %%
# plt.hist(img.ravel(), bins=100, range=(0, 255))
# %%
ret, thresh = cv2.threshold(median, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# %%
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(erosion, kernel, iterations=1)
# %%
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# %%
cv2.imshow("Original Image",img )
cv2.imshow("Otsu Image",thresh )
# cv2.imshow("Eroded Image",erosion )
# cv2.imshow("Eroded + Dilate Image",dilation )
# cv2.imshow("Opened Image",opening )
# cv2.imshow("Closed Image",closing )
cv2.imshow("Median Image",median )


cv2.waitKey(0)
cv2.destroyAllWindows()

# %%

# Median filter
# Non-Local means filter
# erosion
# dilation
# opening
# closing
# top-hat
# black-hat
# Gradient morphological operation