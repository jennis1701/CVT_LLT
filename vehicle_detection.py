import cv2

# Background subtractor (with shadow detection off for stability)
bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows=False)

def detect_vehicles(frame):
    height, width, _ = frame.shape

    # ✅ Region of Interest (focus on lower half - road area)
    roi = frame[int(height * 0.5):height, :]

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(roi)

    # Threshold to remove shadows/noise
    _, thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)

    # ✅ Morphological operations (VERY IMPORTANT)
    thresh = cv2.dilate(thresh, None, iterations=2)
    thresh = cv2.erode(thresh, None, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    vehicle_count = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # ✅ Increased threshold to remove small noise
        if area > 1500:
            x, y, w, h = cv2.boundingRect(cnt)

            # Adjust y coordinate because of ROI cropping
            y = y + int(height * 0.5)

            # Draw bounding box
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            vehicle_count += 1

    return frame, vehicle_count