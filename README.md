# Image-Processing-with-Python

## Project Overview

This repository contains various examples and techniques for performing image processing tasks using Python. As I learn about image processing and its applications, this collection of scripts and modules will expand. The focus is on utilizing popular libraries such as OpenCV and SciPy to explore techniques like thresholding, denoising, edge detection, histogram-based segmentation, and more.

## Table of Contents

- [Installation](#installation)
- [Modules and Examples](#modules-and-examples)
- [License](#license)

## Installation

To run the scripts in this repository, you’ll need to have Python installed along with the required libraries.

### 1. Clone this repository:

```bash
git clone https://github.com/yourusername/Image-Processing-with-Python.git
cd Image-Processing-with-Python ```

### 2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate` ```

### 3. Install dependencies:
```bash
    pip install -r requirements.txt ```

Modules and Examples
1. CLAHE and Thresholding using OpenCV

    Description: This module demonstrates the Contrast Limited Adaptive Histogram Equalization (CLAHE) method for enhancing contrast in images and explores various thresholding techniques.
    Location: images/CLAHE_and_Thresholding.py

2. Denoising and Edge Detection using OpenCV

    Description: Techniques for removing noise and detecting edges within images are covered here, with practical examples using OpenCV’s denoising filters and edge detection algorithms.
    Location: Img/Denoising_and_Edge_Detection.py

3. Denoising Microscope Images in Python

    Description: Special focus on cleaning up microscope images for better analysis, using advanced denoising techniques.
    Location: Denoising_Microscope_Images.py

4. Scratch Assay Analysis with Just 5 Lines of Code in Python

    Description: A streamlined example of scratch assay analysis, often used in cell studies, showing how to perform this task with minimal code.
    Location: Scratch_Assay_Analysis.py

5. Histogram-Based Image Segmentation

    Description: This module covers image segmentation techniques based on histogram analysis, helping separate regions in images for further processing.
    Location: Histogram_Based_Segmentation.py

6. Thresholding and Morphological Operations using OpenCV

    Description: Explores thresholding and morphological operations to refine images, making it easier to isolate features.
    Location: Thresholding_and_Morphological_Operations.py

7. Image Processing using SciPy in Python

    Description: Demonstrates the use of SciPy for image processing, covering techniques complementary to OpenCV’s capabilities.
    Location: Image_Processing_with_SciPy.py

License

This project is licensed under the MIT License. See the LICENSE file for details.
