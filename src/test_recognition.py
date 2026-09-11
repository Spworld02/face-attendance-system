import os
import sys

try:
    import face_recognition
except ImportError:
    raise SystemExit(
        "face_recognition is not installed in the active venv. "
        "Activate the project venv and run: python -m pip install face_recognition"
    )

image_path = os.path.join("data", "test.jpg")
if not os.path.exists(image_path):
    raise SystemExit(
        f"Image not found: {image_path}. Put a clear face photo there first."
    )

# Put any one clear photo of a face in data/ first, e.g. data/test.jpg
image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

print(f"Found {len(face_locations)} face(s)")
if face_encodings:
    print("Embedding vector length:", len(face_encodings[0]))
    print("First 5 values:", face_encodings[0][:5])
else:
    print("No face encodings were generated.")
