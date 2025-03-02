import numpy as np
import cv2
import os

image_path = "Images/coins2.jpeg"

img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to load image. Check file path.")
    exit()

# Convert the image to grayscale for better edge detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise and improve edge detection
blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)

# Use Canny edge detection to find edges in the image
edges = cv2.Canny(blurred, 50, 150)

# Define a kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Use morphological closing to close gaps in the edges
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

# Find contours from the processed image
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours (noise) by setting a minimum area threshold
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

output = img.copy()

cv2.drawContours(output, filtered_contours, -1, (0, 255, 0), 2)

# Count the number of detected coins
num_coins = len(filtered_contours)
print(f"Number of coins detected: {num_coins}")

# Display the image with detected coins
cv2.imshow("Detected Coins", output)

# Save the image with detected coin boundaries
cv2.imwrite("coins_with_boundaries.jpg", output)

# Create a directory to store segmented coin images
os.makedirs("segmented_coins", exist_ok=True)

# Loop through each detected contour
for i, cnt in enumerate(filtered_contours):
    mask = np.zeros_like(gray)

    # Draw the contour on the mask to create a segmentation mask
    cv2.drawContours(mask, [cnt], -1, 255, thickness=cv2.FILLED)
    
    # Extract the coin from the original image using bitwise AND
    segmented_coin = cv2.bitwise_and(img, img, mask=mask)

    x, y, w, h = cv2.boundingRect(cnt)

    # Crop the segmented coin from the original image
    cropped_coin = segmented_coin[y:y+h, x:x+w]

    # Save the cropped coin image
    cv2.imwrite(f"segmented_coins/coin_{i+1}.jpg", cropped_coin)
cv2.waitKey(0)
cv2.destroyAllWindows()
