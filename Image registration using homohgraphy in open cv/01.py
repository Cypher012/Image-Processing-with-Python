"""
1. Import two Images
2. Convert to grayscale
3. Initiate ORB detector
4. Find key points and describe
5. Match Keypoints - Brute force matcher
6. RANSAC (reject bad keypoints)
7. Register two images (use homology)

"""
# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt

# %%
# 1. Import two Images 
im1 = cv2.imread('../images/monkey_distorted.jpg')
im2 = cv2.imread('../images/monkey.jpg')

# 2. Convert to grayscale
img1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv2.ORB_create(500) #type: ignore

# 4. Find key points and describe
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# img3 = cv2.drawKeypoints(img1, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # type: ignore
# img4 = cv2.drawKeypoints(img2, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  # type: ignore
# %%
# 5. Match Keypoints and Descriptors - Brute force matcher

bf =cv2.BFMatcher(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING, crossCheck=True)

matches = bf.match(des1, des2, None)

matches = sorted(matches, key=lambda x:x.distance)

# Draw matches
img_matches = cv2.drawMatches(im1, kp1, im2, kp2, matches[:10], None) # type: ignore

# 6. RANSAC (reject bad keypoints)
points1 = np.zeros((len(matches), 2), dtype=np.float32)
points2 = np.zeros((len(matches), 2), dtype=np.float32)


for i, match in enumerate(matches):
    points1[i, :] = kp1[match.queryIdx].pt
    points2[i, :] = kp2[match.trainIdx].pt


# 7. Register two images (use homology)

h, mask = cv2.findHomography(points1, points2, cv2.RANSAC) 

height, width, channels = im2.shape

img1Reg = cv2.warpPerspective(im1, h, (width, height))



# %%
cv2.imshow("Registered Image", img1Reg)
cv2.imshow("Keypoints matches", img_matches)
# cv2.imshow("img4", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
# %%
