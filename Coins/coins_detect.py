import numpy as np
import cv2
import os

image_path = "/Users/dikshantmahawar/Desktop/Coins/coins3.jpeg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to load image. Check file path.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 1.5)
edges = cv2.Canny(blurred, 50, 150)

kernel = np.ones((5, 5), np.uint8)
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

output = img.copy()
cv2.drawContours(output, filtered_contours, -1, (0, 255, 0), 2)

num_coins = len(filtered_contours)
print(f"Number of coins detected: {num_coins}")

cv2.imshow("Detected Coins", output)
cv2.imwrite("coins_with_boundaries.jpg", output)

os.makedirs("segmented_coins", exist_ok=True)

for i, cnt in enumerate(filtered_contours):
    mask = np.zeros_like(gray)
    cv2.drawContours(mask, [cnt], -1, 255, thickness=cv2.FILLED)
    
    segmented_coin = cv2.bitwise_and(img, img, mask=mask)

    x, y, w, h = cv2.boundingRect(cnt)
    cropped_coin = segmented_coin[y:y+h, x:x+w]

    cv2.imwrite(f"segmented_coins/coin_{i+1}.jpg", cropped_coin)

cv2.waitKey(0)
cv2.destroyAllWindows()

