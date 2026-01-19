Intelligent Pesticide Detection System (OpenCV-Based)

Overview
This project implements a basic pesticide detection system using traditional computer vision techniques.
The objective is to detect pesticide containers from images using OpenCV, without relying on deep learning models.
The project was developed to understand how classical image processing methods can be applied to real-world agricultural safety problems.

Problem Statement
In agricultural environments, pesticide containers need to be identified and monitored to avoid misuse and unsafe handling. Manual identification is time-consuming and error-prone. This project explores a simple and lightweight computer vision approach for detecting pesticide bottles using image processing techniques.

Methodology
The system is built using OpenCV and follows these steps:
-Image acquisition from stored images or camera input
-Image preprocessing such as resizing, color conversion, and noise reduction
-Feature-based detection using contours and shape analysis
-Bounding box generation around detected pesticide containers
-Visualization of detection results
The focus of this project is on understanding image processing logic rather than achieving high accuracy through learning-based models.

Technologies Used
-Python
-OpenCV
-NumPy
-Google Colab / Local Python Environment

Dataset
The project uses sample pesticide container images collected from online sources for testing and experimentation. The dataset is small and intended only for demonstrating the detection pipeline.

Results
-The system can detect pesticide containers in simple backgrounds
-Works best when object edges are clear and lighting conditions are good
-Performance degrades in complex scenes or cluttered backgrounds
-These results highlight both the strengths and limitations of classical computer vision techniques.

Key Learnings
-Practical use of OpenCV for object detection
-Understanding contour detection and image preprocessing
-Limitations of non-learning-based vision systems
-Importance of data quality and controlled environments

Limitations
-Not robust to background variations
-Sensitive to lighting conditions
-Cannot generalize well across different bottle shapes
-No real-time deployment or optimization for edge devices

Future Improvements
-Integrate deep learning–based object detection for better accuracy
-Expand dataset with more diverse images
-Combine OpenCV preprocessing with ML models
-Deploy on embedded platforms like Raspberry Pi

How to Run
-Clone the repository
-Install required Python libraries
-Run the main Python script or notebook
-Provide an input image containing pesticide containers
-View detection output with bounding boxes

Author
Navya Bommisetty
