import cv2
import numpy as np
import time
import os

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Camera not accessible")

save_cooldown = 3  # seconds between captures
last_saved_time = 0

# Create folder if not exists
if not os.path.exists("fire_snapshots"):
    os.makedirs("fire_snapshots")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # ALWAYS mirrored

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Fire color range
    lower_fire = np.array([0, 120, 200])
    upper_fire = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    fire_detected = False

    for cnt in contours:
        if cv2.contourArea(cnt) > 1500:
            fire_detected = True
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
            break

    if fire_detected:
        overlay = frame.copy()
        overlay[:] = (0, 0, 255)
        frame = cv2.addWeighted(overlay, 0.25, frame, 0.75, 0)

        cv2.putText(
            frame,
            "FIRE DETECTED!",
            (40, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.6,
            (255, 255, 255),
            4
        )

        # Save snapshot
        if time.time() - last_saved_time > save_cooldown:
            filename = f"fire_snapshots/fire_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            last_saved_time = time.time()

            cv2.putText(
                frame,
                "SNAPSHOT SAVED!",
                (40, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 255, 255),
                3
            )

    cv2.imshow("Fire Detection - Auto Snapshot", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
