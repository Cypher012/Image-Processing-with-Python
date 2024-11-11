# %%
from skimage.filters.rank import entropy
from skimage.morphology import disk
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu
import glob
# %%
img = io.imread("../images/scratch.jpg")
entropy_img = entropy(img, disk(7))
plt.imshow(entropy_img, cmap='gray')
# %%
thresh = threshold_otsu(entropy_img)
print(thresh)
# %%
binary = entropy_img <= thresh
plt.imshow(binary, cmap='gray')
# %%
percentage_of_white = (np.sum(binary == 1)/((np.sum(binary == 1)) + np.sum(binary == 0)) * 100)
# %%
print(f"The percent bright pixels is {percentage_of_white:.2f}%")

# %%
time = 0
time_list = []
area_list = []
path = "../images/scratch_assay/*.*"
# %%
for file in glob.glob(path):
    img = io.imread(file)
    entropy_img = entropy(img, disk(10))
    plt.imshow(entropy_img, cmap='gray')
    thresh = threshold_otsu(entropy_img)
    # print(f"thresh: {thresh}")
    binary = entropy_img <= thresh
    plt.imshow(binary, cmap='gray')
    percentage_of_white = (np.sum(binary == 1)/((np.sum(binary == 1)) + np.sum(binary == 0)) * 100)
    scratch_area = np.sum(binary == True)
    # print(f"time = {time}, scratch_area: {scratch_area}")
    # print(f"The percent of bright pixels is {percentage_of_white:.2f}%")
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1
# %%
plt.plot(time_list, area_list,'bo')
# %%
from scipy.stats import linregress
# %%
slope, intercept, r_value, p_value, std_err = linregress(time_list, area_list)
print(f"y = {slope}x  + {intercept}")
print("R/N{SUPERSCRIPT TWO}= ", r_value ** 2)
# %%
