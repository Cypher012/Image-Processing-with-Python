# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %%
img = cv2.imread("../images/Alloy.jpg", 0)
eq_img = cv2.equalizeHist(img)
# %%
plt.hist(eq_img.ravel(), bins=100, range=(100, 255))

# %%

# CLAHE - Contrast Limited Adaptive Histogram Eqalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

plt.hist(cl_img.ravel(), bins=100, range=(100, 255))

# %%
ret1, thresh1 = cv2.threshold(cl_img, 180, 150, cv2.THRESH_BINARY)
# _, thresh2 = cv2.threshold(cl_img, 180, 255, cv2.THRESH_BINARY_INV)
ret2, thresh2 = cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# %%
cv2.imshow('img',img)
cv2.imshow('Binary threshold 1',thresh1)
cv2.imshow('Binary threshold 2',thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
# Apply adaptive thresholding
thresh_mean = cv2.adaptiveThreshold(cl_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)

thresh_gaussian = cv2.adaptiveThreshold(cl_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)   
# %%
cv2.imshow('img',img)
cv2.imshow('Thresh mean',thresh_mean)
cv2.imshow('thresh_gaussian',thresh_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
