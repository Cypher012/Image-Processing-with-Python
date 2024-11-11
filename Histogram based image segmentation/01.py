# %%
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.metrics import peak_signal_noise_ratio
from skimage.util import random_noise
# %%

# Load the noisy image
img = io.imread("../images/BSE_Google_noisy.jpg").astype(float)
print("Image shape:", img.shape)

# %%

# Estimate the noise standard deviation
sigma_est = np.mean(estimate_sigma(img, channel_axis=-1))

# Define patch parameters
patch_kw = dict(
    patch_size=5, patch_distance=6, channel_axis=-1
)

# Apply non-local means denoising
denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=False, **patch_kw)
# %%

# Display the result
plt.imshow(denoise, cmap='gray')
plt.title("Denoised Image")
plt.show()
