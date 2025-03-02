import numpy as np
import cv2
import glob
import os

input_dir = "/Users/dikshantmahawar/Desktop/Panaroma/Images/"
output_dir = "/Users/dikshantmahawar/Desktop/Panaroma/output/"

os.makedirs(output_dir, exist_ok=True)

image_paths = sorted(glob.glob(os.path.join(input_dir, "*.jpeg")))

images = []

# Load images from the specified directory
for path in image_paths:
    img = cv2.imread(path)  # Read image
    if img is not None:
        images.append(img)  
    else:
        print(f"Warning: Unable to load image {path}")  

# Ensure there are at least two images for stitching
if len(images) < 2:
    print("Error: At least 2 images are required for stitching.")
    exit()

# Initialize SIFT (Scale-Invariant Feature Transform) detector
sift = cv2.SIFT_create()

# Initialize Brute-Force Matcher with L2 norm
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

# Detect and draw keypoints on each image
for idx, img in enumerate(images):
    keypoints, descriptors = sift.detectAndCompute(img, None)  
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, None, color=(255, 0, 0), 
                                           flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT) 
    cv2.imwrite(f"{output_dir}/image_{idx+1}.png", img_with_keypoints)  

# Feature matching between consecutive images
for i in range(len(images) - 1):
    img1, img2 = images[i], images[i + 1]
    
    # Compute keypoints and descriptors for both images
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # Match descriptors between images
    matches = sorted(bf.match(des1, des2), key=lambda x: x.distance)  

    # Draw the first 100 matches
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:100], None, 
                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Save the match visualization
    match_filename = os.path.join(output_dir, f"matches_{i+1}_{i+2}.png")
    cv2.imwrite(match_filename, img_matches)

stitcher = cv2.Stitcher_create()

# Perform image stitching
status, stitched = stitcher.stitch(images)

# Check if stitching was successful
if status == cv2.Stitcher_OK:
    print("Stitching successful. Saving output images...")
    cv2.imwrite(os.path.join(output_dir, "stitched_output.png"), stitched)  
    cv2.imshow("Final Stitched Image", stitched) 
else:
    print(f"Stitching failed with error code: {status}") 

cv2.waitKey(0)
cv2.destroyAllWindows()
