# 🚦 Smart Traffic Monitoring and Lane Detection System

## 📌 Project Overview
This project is a computer vision-based traffic monitoring system that detects lane boundaries and estimates vehicle count from uploaded traffic videos. It is designed as part of a smart city initiative to monitor congestion and lane usage using CCTV footage.

The system uses classical image processing techniques to analyze video frames in real time through an interactive Streamlit web application.

---

## 🎯 Objectives
- Detect lane boundaries using edge detection and line detection techniques
- Identify and count moving vehicles in traffic videos
- Provide performance analysis without requiring ground truth data
- Build an interactive UI for real-time demonstration

---

## 🧠 Techniques Used

- Edge Detection: Canny Edge Detection  
- Line Detection: Hough Transform  
- Background Subtraction (MOG2)  
- Contour Detection  
- Morphological Operations (Dilation & Erosion)  
- Temporal Smoothing for stability  

---

## 🏗️ Project Structure

smart-traffic-system/
│
├── app.py                 # Streamlit UI  
├── lane_detection.py      # Lane detection logic  
├── vehicle_detection.py   # Vehicle detection logic  
├── utils.py               # Helper functions  
├── videos/                # Sample videos  
└── requirements.txt       # Dependencies  

---

## ⚙️ Installation

1. Clone the repository or download the project folder

2. Install dependencies:
pip install -r requirements.txt

3. Run the application:
streamlit run app.py

---

## 🚀 Features

- 📹 Upload and process traffic videos  
- 🛣️ Lane detection using edge and line detection  
- 🚗 Vehicle detection using motion-based techniques  
- 📊 Real-time performance metrics:
  - Detection Consistency Score  
  - Processing FPS  
  - Average Vehicles per Frame  
- 🌗 Lighting condition selection (Day/Night/Low Light)  

---

## 📊 Performance Metrics

Since ground truth data is not available for user-uploaded videos, the system evaluates performance using:

- Detection Consistency Score  
  Measures stability of vehicle detection across frames  

- Processing FPS (Frames Per Second)  
  Measures speed of the system  

- Average Vehicles per Frame  
  Indicates detection density  

---

## ⚠️ Limitations

- May overcount vehicles (no tracking implemented)  
- Performance may decrease in low-light conditions  
- Sensitive to shadows and background noise  
- Accuracy depends on video quality and camera angle  

---

## 🔧 Improvements Implemented

- Region of Interest (ROI) to focus on road area  
- Noise reduction using Gaussian Blur  
- Morphological filtering to stabilize detection  
- Temporal smoothing to improve consistency  

---

## 🔮 Future Enhancements

- Vehicle tracking to avoid double counting  
- Lane-wise vehicle counting  
- Deep learning-based detection (YOLO)  
- Real-time CCTV integration  
- Graph visualization of traffic trends  

---

## 🎓 Conclusion

This project demonstrates how classical computer vision techniques can be applied to solve real-world traffic monitoring problems. It highlights the trade-offs between simplicity and accuracy, and provides a scalable foundation for advanced intelligent traffic systems.

---

## 🙌 Acknowledgment

Developed as part of an academic mini project for learning computer vision and real-time system design.