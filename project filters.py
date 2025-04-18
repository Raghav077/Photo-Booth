import cv2
import pandas as pd
from datetime import datetime
import os

# Create output folder
os.makedirs("photos", exist_ok=True)

# Available filters
filters = ['normal', 'grayscale', 'blur', 'sepia']
filter_index = 0

# Photo log
log = []

# Sepia filter using OpenCV only
def apply_sepia(frame):
    # Split the channels
    b, g, r = cv2.split(frame)

    tr = 0.393 * r + 0.769 * g + 0.189 * b
    tg = 0.349 * r + 0.686 * g + 0.168 * b
    tb = 0.272 * r + 0.534 * g + 0.131 * b

    tr[tr > 255] = 255
    tg[tg > 255] = 255
    tb[tb > 255] = 255

    sepia = cv2.merge([tb.astype('uint8'), tg.astype('uint8'), tr.astype('uint8')])
    return sepia

# Apply selected filter
def apply_filter(frame, filter_name):
    if filter_name == 'grayscale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_name == 'blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filter_name == 'sepia':
        return apply_sepia(frame)
    return frame

# Webcam capture
cap = cv2.VideoCapture(0)
print("Press 'f' to switch filter, 's' to save, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_filter = filters[filter_index]
    filtered = apply_filter(frame, current_filter)

    # Convert grayscale to BGR for consistent display
    if current_filter == 'grayscale':
        display = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)
    else:
        display = filtered

    # Show filter name
    cv2.putText(display, f'Filter: {current_filter}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Photo Booth", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('f'):
        filter_index = (filter_index + 1) % len(filters)
    elif key == ord('s'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'photos/photo_{timestamp}.jpg'
        cv2.imwrite(filename, display)
        log.append({"Time": timestamp, "Filter": current_filter, "Filename": filename})
        print(f"Photo saved: {filename}")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Save metadata
df = pd.DataFrame(log)
df.to_csv("photo_log.csv", index=False)
print("Photo log saved to photo_log.csv")
