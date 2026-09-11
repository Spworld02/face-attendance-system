import os
import cv2

# Load OpenCV's pre-trained face detector (comes bundled with opencv-python)
cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')

if not os.path.exists(cascade_path):
    raise FileNotFoundError(
        f"Face cascade file not found at: {cascade_path}. "
        "Reinstall OpenCV with its bundled data files."
    )

face_cascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Face detection started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Detection works on grayscale images — faster & more accurate
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,      # how much the image size is reduced at each scale
        minNeighbors=5,       # higher = fewer false positives
        minSize=(60, 60)      # ignore detections smaller than this
    )

    # Draw a rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
