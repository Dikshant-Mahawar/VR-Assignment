import numpy as np
import cv2
import glob
import os

input_dir = "/Users/dikshantmahawar/Desktop/Panaroma/Images/"
output_dir = "/Users/dikshantmahawar/Desktop/Panaroma/output/"

os.makedirs("/Users/dikshantmahawar/Desktop/Panaroma/output/", exist_ok=True)

image_paths = sorted(glob.glob(os.path.join("/Users/dikshantmahawar/Desktop/Panaroma/Images/", "*.jpeg")))
images = []

for path in image_paths:
    img = cv2.imread(path)
    if img is not None:
        images.append(img)
    else:
        print(f"Warning: Unable to load image {path}")

if len(images) < 2:
    print("Error: At least 2 images are required for stitching.")
    exit()

sift = cv2.SIFT_create()
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

for idx, img in enumerate(images):
    keypoints, descriptors = sift.detectAndCompute(img, None)
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    cv2.imwrite(f"{output_dir}/image_{idx+1}.png", img_with_keypoints)

for i in range(len(images) - 1):
    img1, img2 = images[i], images[i + 1]
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:100], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    match_filename = os.path.join("/Users/dikshantmahawar/Desktop/Panaroma/output/", f"matches_{i+1}_{i+2}.png")
    cv2.imwrite(match_filename, img_matches)

stitcher = cv2.Stitcher_create()
status, stitched = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    print("Stitching successful. Saving output images...")
    cv2.imwrite(os.path.join("/Users/dikshantmahawar/Desktop/Panaroma/output/", "stitched_output.png"), stitched)
    cv2.imshow("Final Stitched Image", stitched)
else:
    print(f"Stitching failed with error code: {status}")

cv2.waitKey(0)
cv2.destroyAllWindows()
