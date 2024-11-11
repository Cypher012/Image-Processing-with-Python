# %%
from skimage import io
from scipy import ndimage as nd
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
# %%

img = (io.imread("../images/denoising/noisy_img.jpg")).astype(float)
plt.imshow(img)
# %%

gaussian_img = nd.gaussian_filter(img, sigma=3)

plt.imshow(gaussian_img)
# %%
median_img = nd.median_filter(img, size=3)
plt.imshow(median_img)


# %%
from skimage.restoration import estimate_sigma, denoise_nl_means
import numpy as np

# Corrected line with closing parenthesis
sigma_est = np.mean(estimate_sigma(img))
print(f'estimated noise standard deviation = {sigma_est}')

# Apply denoising
denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False, patch_size=5, patch_distance=3, multichannel=True)

# %%
