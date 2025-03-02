# Coin Detection & Panorama Stitching

## Overview
This project tackles two key computer vision tasks:
1. **Coin Detection & Segmentation** – Identifying, segmenting, and counting coins in an image.
2. **Panorama Stitching** – Merging multiple overlapping images into a seamless panorama.

Both tasks leverage **OpenCV** for image processing and **NumPy** for numerical computations.

---

## 1. Coin Detection & Segmentation

### **Usage Instructions**
1. Place images of scattered Indian coins inside the `Coins/Images/` directory.
2. Run the script:
   ```bash
   python Coins/coins_detect.py
   ```
3. The script performs the following:
   - Detects coins using **edge and contour detection**.
   - Segments each coin using **region-based segmentation**.
   - Counts the total number of detected coins.
   - Saves and displays the results.
4. Output images are stored in the `Coins/segmented_coins/` folder.

### **Techniques Used**
- **Edge Detection** – Canny edge detection highlights coin boundaries.
- **Contour Detection** – Extracts coin shapes.
- **Region-Based Segmentation** – Uses bounding boxes and masks for precise segmentation.

### **Observations**
✅ Accurately detects and counts coins.
✅ Handles lighting variations well.
⚠️ May struggle with reflections or overlapping coins.

---

## 2. Panorama Stitching

### **Usage Instructions**
1. Place all input images for stitching inside the `Panorama/Images/` directory.
2. Run the script:
   ```bash
   python Panorama/panorama_final.py
   ```
3. The script performs the following:
   - Reads and preprocesses images from `Panorama/Images/`.
   - Extracts key points using **SIFT (Scale-Invariant Feature Transform)**.
   - Aligns and stitches images using **OpenCV’s Stitcher module**.
   - Saves the final stitched image in the `Panorama/output/` folder.

### **Techniques Used**
- **Feature Detection** – SIFT extracts key points and descriptors.
- **Feature Matching** – Aligns images based on overlapping key points.
- **Image Blending** – Seamlessly merges images into a panorama.

### **Observations**
✅ Successfully stitches overlapping images.
✅ Produces seamless panoramas with proper image alignment.
⚠️ Requires sufficient overlap between images for accuracy.

---

## Project Structure
```
|-- Coins/               # Coin Detection & Segmentation
|   |-- coins_detect.py  # Code for coin detection
|   |-- Images/          # Contains images of coins
|   |-- segmented_coins/ # Contains segmented images of the coins
|   |-- myenv/           # Python environment
|
|-- Panorama/            # Panorama Stitching
|   |-- panorama_final.py # Code for stitching overlapping images
|   |-- Images/          # Contains overlapping images for stitching
|   |-- output/          # Contains key points detected and stitched images
|   |-- myenv/           # Python environment
|
|-- README.md            # Documentation
```

---

## Installation
Ensure you have the required dependencies installed:
```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```

---

## Additional Notes
- Place input images in the correct directories before running the scripts.
- The scripts run automatically without manual intervention.
- All output images are saved in their respective `output/` folders.

For troubleshooting, verify file paths and dependencies.

Happy coding! 🚀

