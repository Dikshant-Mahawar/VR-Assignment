# Coin Detection and Panorama Stitching

## Project Overview
This project consists of two main tasks:
1. **Coin Detection and Segmentation**: Detect, segment, and count the number of coins in an image.
2. **Panorama Stitching**: Stitch multiple overlapping images into a single panorama.

The implementation uses **OpenCV** for computer vision tasks and **NumPy** for numerical operations.

---

## 1. Coin Detection and Segmentation

### **How to Run the Code**
1. Place the input image containing scattered Indian coins in the root directory and name it `coins.jpeg`.
2. Run the following command in the terminal or command prompt:
   ```bash
   python coin_detection.py
   ```
3. The script will:
   - Detect coins using **edge detection** and **contour detection**.
   - Segment each coin using **region-based segmentation**.
   - Count the total number of detected coins.
   - Save and display the results.
4. The output images `Detected_coins.jpeg` will be saved in the `output/` folder.

### **Methods Used**
- **Edge Detection**: Used Canny edge detection to highlight the boundaries of coins.
- **Contour Detection**: Extracts coin shapes based on detected edges.
- **Region-Based Segmentation**: Each coin is segmented using its bounding box and mask.

### **Results & Observations**
- The program accurately detects and counts the coins.
- Some coins may have partial segmentation due to reflections or overlapping regions.
- The algorithm is robust to lighting variations but may require fine-tuning for complex backgrounds.

---

## 2. Panorama Stitching

### **How to Run the Code**
1. Place all input images for panorama stitching in the `images/` folder.
2. Run the following command:
   ```bash
   python panorama.py
   ```
3. The script will:
   - Read and preprocess all images in the `images/` folder.
   - Extract key points using **SIFT (Scale-Invariant Feature Transform)**.
   - Align and stitch images together using **OpenCV's Stitcher module**.
   - Save and display the final stitched image.
   - Save both the stitched image and stitched image with keypoints in the `output/` folder.

### **Methods Used**
- **Feature Detection**: SIFT is used to extract key points and descriptors from the images.
- **Feature Matching**: The algorithm aligns images based on overlapping key points.
- **Image Blending**: Merges the images seamlessly to create a panorama.

### **Results & Observations**
- The program successfully stitches overlapping images into a seamless panorama.
- Requires sufficient overlap between images for accurate stitching.
- Performance may vary based on image resolution and feature-rich areas.

---

## Folder Structure
```
|-- images/               # Input images for panorama stitching
|-- output/               # Output images (Detected coins, segmented coins, panorama results)
|-- coin_detection.py     # Coin detection & segmentation script
|-- panorama.py          # Panorama stitching script
|-- coins.jpeg           # coins image
|-- README.md            # This documentation file
```

---

## Dependencies
Ensure you have the required Python libraries installed:
```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```

---

## Notes
- Ensure all images are placed in the correct directories before running the scripts.
- The scripts are designed to run without additional intervention.
- All visual outputs (detection, segmentation, counting, and panorama stitching) are saved in the `output/` folder.

If you encounter any issues, please check the file paths and dependencies before running the scripts.

Happy coding! 🚀
