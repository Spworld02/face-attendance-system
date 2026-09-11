import cv2
import face_recognition
import pickle
import csv
import os
from datetime import datetime

DATA_FILE = "models/encodings.pkl"
ATTENDANCE_FILE = "data/attendance.csv"
MATCH_THRESHOLD = 0.5  # lower = stricter matching

def load_known_faces():
    if not os.path.exists(DATA_FILE):
        print("No enrolled faces found. Run enroll.py first.")
        exit()
    with open(DATA_FILE, "rb") as f:
        return pickle.load(f)

def already_marked_today(name):
    if not os.path.exists(ATTENDANCE_FILE):
        return False
    today = datetime.now().strftime("%Y-%m-%d")
    with open(ATTENDANCE_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2 and row[0] == name and row[1].startswith(today):
                return True
    return False

def mark_attendance(name):
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.exists(ATTENDANCE_FILE)
    with open(ATTENDANCE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Timestamp"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([name, timestamp])
    print(f"Attendance marked: {name} at {timestamp}")

def run_recognition():
    known_data = load_known_faces()
    known_encodings = known_data["encodings"]
    known_names = known_data["names"]

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Recognition started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize for faster processing, convert BGR->RGB
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            distances = face_recognition.face_distance(known_encodings, face_encoding)
            name = "Unknown"

            if len(distances) > 0:
                # distances is a numpy array
                best_match_index = distances.argmin()
                if distances[best_match_index] < MATCH_THRESHOLD:
                    name = known_names[best_match_index]
                    if not already_marked_today(name):
                        mark_attendance(name)

            # Scale back up face locations (since frame was resized to 0.25x)
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        cv2.imshow("Attendance - Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_recognition()
