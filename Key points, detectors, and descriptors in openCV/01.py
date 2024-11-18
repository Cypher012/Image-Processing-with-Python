# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Harris Algorithm cv2.cornerHarris()
'''

# %%
# Load the image in grayscale
img = cv2.imread("../images/grains.jpg", 0)

# Convert to a 3-channel image to allow color marking
img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# Convert image to float32 for corner detection
gray = np.float32(img)

# Apply Harris Corner Detection
harris = cv2.cornerHarris(gray, 2, 3, 0.04) # type: ignore

# Mark the corners in red
img_color[harris > 0.01 * harris.max()] = [0, 0, 255]

# %%
# Display the image with marked corners
plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()


# %%
'''
Shi-Tomasi corner detection algorithm
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
# Load the image in grayscale

img = cv2.imread("../images/grains.jpg", 0)

gray = np.float32(img)

#input image, #points, quality level (0 < qualityLevel ≤ 1), min euclidean dist. between detected points
corners = cv2.goodFeaturesToTrack(gray,50,0.05,10) # type: ignore
corners = np.int64(corners)
# %%

for i in corners: # type: ignore
    x,y = i.ravel()   
    cv2.circle(img,(x,y),5,255,-1) # type: ignore

cv2.imshow('Corners',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
'''
FAST Feature Detector in OpenCV
'''
# %%
import cv2
import matplotlib.pyplot as plt
# %%
# Load the image
img = cv2.imread('../images/grains.jpg', 0)
# %%

# Create a FAST detector object
fast = cv2.FastFeatureDetector_create(threshold=50, nonmaxSuppression=True) # type: ignore

# Detect keypoints
keypoints = fast.detect(img, None)

# Draw keypoints on the original image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, color=(255, 0, 0)) # type: ignore
# %%
# Display the image
plt.imshow(cv2.cvtColor(img_with_keypoints, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
# %%
'''
ORB(Oriented FAST and Rotated Brief)
'''
# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread('../images/monkey.jpg', cv2.IMREAD_GRAYSCALE)
 
# Initiate ORB detector
orb = cv2.ORB_create(50) #type: ignore
 
kp, des = orb.detectAndCompute(img, None)
 
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # type: ignore
# %%
# Display the image
cv2.imshow('ORB', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
