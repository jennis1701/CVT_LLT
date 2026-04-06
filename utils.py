import cv2
import numpy as np

# ✅ Resize frame (used for faster processing)
def resize_frame(frame, width=640, height=360):
    return cv2.resize(frame, (width, height))


# ✅ Apply Gaussian Blur (reduces noise)
def apply_blur(frame):
    return cv2.GaussianBlur(frame, (5, 5), 0)


# ✅ Region of Interest (focus on road area)
def get_roi(frame):
    height, width, _ = frame.shape
    roi = frame[int(height * 0.5):height, :]
    return roi


# ✅ Draw text on frame (for labels)
def draw_text(frame, text, position=(10, 30)):
    cv2.putText(
        frame,
        text,
        position,
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )
    return frame


# ✅ Smooth vehicle count (temporal smoothing)
def smooth_count(prev_count, current_count, alpha=0.85):
    return int(alpha * prev_count + (1 - alpha) * current_count)


# ✅ Calculate performance metrics
def calculate_metrics(frame_counts, start_time, end_time):
    if len(frame_counts) == 0:
        return 0, 0, 0

    mean = np.mean(frame_counts)
    std = np.std(frame_counts)

    consistency = 1 - (std / mean) if mean != 0 else 0
    fps = len(frame_counts) / (end_time - start_time)
    avg_vehicles = mean

    return consistency, fps, avg_vehicles