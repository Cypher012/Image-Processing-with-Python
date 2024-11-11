# %%
# from scipy import misc
from skimage import io
import numpy as np
from numpy import ndarray
import matplotlib.pyplot as plt
# %%
img = io.imread("../Img/image1.jpg", as_gray=True)
# %%
from skimage.transform import rescale, resize, downscale_local_mean
# %%
rescaled_img = rescale(img, 1.0/4.0, anti_aliasing = True)
resized_img = resize(img, (200,200))
downscale_img = downscale_local_mean(img, (4,3))
# %%
plt.imshow(downscale_img, cmap="gray")
# %%
img = io.imread("../images/test_image_cropped.jpg", as_gray=True)
# %%
from typing import Literal
from skimage.filters import roberts, sobel, scharr, prewitt
# %%
def filters(filter: Literal['roberts', 'sobel', "scharr", 'prewitt']) -> ndarray :
    edge = None 
    if filter == "roberts":
        edge = roberts(img)
    elif filter == "sobel":
        edge = sobel(img)
    elif filter == "scharr":
        edge = scharr(img)
    elif filter == "prewitt":
        edge = prewitt(img)
    return edge

plt.imshow(img, cmap='gray')
plt.title(f'Img')


# %%
edge = filters('scharr')
plt.imshow(edge, cmap='gray')
plt.title(f'scharr')
# %%
from skimage.feature import canny

# %%
canny = canny(img, sigma= 3)
plt.imshow(canny, cmap='gray')
plt.title(f'Canny')
# %%
from skimage import restoration
psf = np.ones((3,3)) / 9
# %%
# REAL WORD SCENARIO

import matplotlib.pyplot as plt
from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk
# %%
img = io.imread("../images/scratch.jpg")
entr_img = entropy(img, disk(3))
# %%
plt.imshow(entr_img, cmap="gray")
# %%
from skimage.filters import try_all_threshold
# %%
fig, ax = try_all_threshold(entr_img, figsize=(10, 8), verbose=False)
plt.show()
# %%
from skimage.filters import threshold_otsu
thresh = threshold_otsu(entr_img)
# %%
binary = entr_img <= thresh
plt.imshow(binary, cmap='gray')
# %%
percentage_of_white = ((np.sum(binary==1))/(np.sum(binary == 1) + np.sum(binary == 0))) * 100
print(f"The percent bright pixels is {percentage_of_white:.2f}%")
# %%
