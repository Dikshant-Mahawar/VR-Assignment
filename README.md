# Coin Detection & Panorama Stitching

## Overview
This project tackles two key computer vision tasks:
1. **Coin Detection & Segmentation** – Identifying, segmenting, and counting coins in an image.
2. **Panorama Stitching** – Merging multiple overlapping images into a seamless panorama.

Both tasks leverage **OpenCV** for image processing and **NumPy** for numerical computations.

---

## 1. Coin Detection & Segmentation

### **Usage Instructions**
1. Place an image of scattered Indian coins in the root directory and name it `coins.jpeg`.
2. Run the script:
   ```bash
   python coin_detection.py
   ```
3. The script performs the following:
   - Detects coins using **edge and contour detection**.
   - Segments each coin using **region-based segmentation**.
   - Counts the total number of detected coins.
   - Saves and displays the results.
4. Output images are stored in the `output/` folder.

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
1. Place all input images for stitching inside the `images/` folder.
2. Run the script:
   ```bash
   python panorama.py
   ```
3. The script performs the following:
   - Reads and preprocesses images from `images/`.
   - Extracts key points using **SIFT (Scale-Invariant Feature Transform)**.
   - Aligns and stitches images using **OpenCV’s Stitcher module**.
   - Saves the final stitched image in the `output/` folder.

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
|-- images/              # Input images for panorama stitching
|-- output/              # Output images (Detected coins, segmented coins, panorama results)
|-- coin_detection.py    # Coin detection & segmentation script
|-- panorama.py         # Panorama stitching script
|-- coins.jpeg          # Sample coin image
|-- README.md           # Documentation
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
- All output images are saved in the `output/` folder.

For troubleshooting, verify file paths and dependencies.

Happy coding! 🚀

