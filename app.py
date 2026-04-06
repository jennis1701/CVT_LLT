import streamlit as st
import cv2
import tempfile
import time
import numpy as np
from lane_detection import detect_lanes
from vehicle_detection import detect_vehicles

st.title("🚦 Smart Traffic Monitoring System")

# Lighting condition (for analysis)
lighting = st.selectbox("Lighting Condition", ["Day", "Night", "Low Light"])
st.write(f"Selected Lighting: {lighting}")

uploaded_file = st.file_uploader("Upload Traffic Video", type=["mp4", "avi"])

if uploaded_file is not None:
    # Save uploaded video to temp file
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)

    stframe1, stframe2 = st.columns(2)

    original_frame = stframe1.empty()
    processed_frame = stframe2.empty()

    vehicle_count = 0
    frame_counts = []
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 360))

        # Lane detection
        lane_frame = detect_lanes(frame)

        # Vehicle detection
        processed, count = detect_vehicles(lane_frame)

        vehicle_count += count
        frame_counts.append(count)

        # Display frames
        original_frame.image(frame, channels="BGR", caption="Original Video")
        processed_frame.image(processed, channels="BGR", caption="Processed Video")

    cap.release()
    end_time = time.time()

    # Show total vehicles
    st.success(f"Total Vehicles Detected: {vehicle_count}")

    # 📊 Performance Metrics
    if len(frame_counts) > 0:
        mean = np.mean(frame_counts)
        std = np.std(frame_counts)

        consistency = 1 - (std / mean) if mean != 0 else 0
        fps = len(frame_counts) / (end_time - start_time)
        avg_vehicles = mean

        st.subheader("📊 Performance Metrics")
        st.info(f"Detection Consistency Score: {consistency:.2f}")
        st.info(f"Processing FPS: {fps:.2f}")
        st.info(f"Average Vehicles per Frame: {avg_vehicles:.2f}")