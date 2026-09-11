import cv2
import face_recognition
import pickle
import os

DATA_FILE = "models/encodings.pkl"

def load_known_faces():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    return {"encodings": [], "names": []}

def save_known_faces(data):
    os.makedirs("models", exist_ok=True)
    with open(DATA_FILE, "wb") as f:
        pickle.dump(data, f)

def enroll_person(name):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print(f"Enrolling '{name}'. Press SPACE to capture, 'q' to cancel.")
    captured_encoding = None
    clicked = {"flag": False}

    def _on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            clicked["flag"] = True

    window_name = "Enroll - Press SPACE to capture"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, _on_mouse)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Overlay simple instructions on the frame so users know what to press
        disp = frame.copy()
        cv2.putText(disp, "Press SPACE or click to capture, 'q' to cancel", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow(window_name, disp)

        key = cv2.waitKey(10) & 0xFF
        should_capture = False
        if key in (32,):  # SPACE
            should_capture = True
        if key in (ord('c'), ord('C')):
            should_capture = True
        if clicked["flag"]:
            should_capture = True

        if should_capture:
            clicked["flag"] = False
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)

            if len(face_locations) != 1:
                print(f"Need exactly 1 face, found {len(face_locations)}. Try again.")
                continue

            encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            captured_encoding = encodings[0]
            print("Face captured successfully!")
            break

        if key in (ord('q'), ord('Q'), 27):
            print("Enrollment cancelled.")
            break

    cap.release()
    cv2.destroyAllWindows()

    if captured_encoding is not None:
        data = load_known_faces()
        data["encodings"].append(captured_encoding)
        data["names"].append(name)
        save_known_faces(data)
        print(f"'{name}' enrolled and saved to {DATA_FILE}")

if __name__ == "__main__":
    person_name = input("Enter name/roll number to enroll: ")
    enroll_person(person_name)
