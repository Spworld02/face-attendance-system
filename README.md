# AI-Based Smart Face Attendance System

A real-time face recognition attendance system built with Python, OpenCV, and `face_recognition`. Detects and recognizes enrolled faces via webcam, automatically marks attendance (once per day per person), and provides a Streamlit dashboard to view and export records.

## Features

- Live face detection via webcam (OpenCV)
- Face recognition using 128-d face embeddings (`face_recognition` / dlib)
- One-time enrollment flow for registering new people
- Automatic attendance logging to CSV (duplicate-proof — one mark per person per day)
- Streamlit dashboard with name/date filters, summary metrics, and CSV export

## Tech Stack

- Python 3.12
- OpenCV (`opencv-python`)
- `face_recognition` (dlib-based face embeddings)
- Streamlit + pandas (dashboard)

## Project Structure

```
face-attendance-system/
├── data/               # attendance.csv (not tracked in git)
├── models/             # encodings.pkl (not tracked in git)
├── src/
│   ├── enroll.py        # register a new person's face
│   ├── recognize.py     # live recognition + attendance marking
│   ├── dashboard.py      # Streamlit dashboard
│   └── check_enrolled.py # quick check of enrolled people
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repo and enter the project folder:
   ```bash
   git clone https://github.com/YOUR-USERNAME/face-attendance-system.git
   cd face-attendance-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**1. Enroll a person:**
```bash
python src/enroll.py
```
Enter their name, then press SPACE when their face is clearly visible in the webcam window.

**2. Run live recognition & attendance marking:**
```bash
python src/recognize.py
```
Recognized faces are shown with a green box and name; unrecognized faces show a red box marked "Unknown". Attendance is logged to `data/attendance.csv`.

**3. View the dashboard:**
```bash
streamlit run src/dashboard.py
```
Opens in your browser at `http://localhost:8501` with filters, summary stats, and CSV export.

## Notes

- Enrolled face data (`models/encodings.pkl`) and attendance logs (`data/attendance.csv`) are excluded from version control via `.gitignore` for privacy.
- Recognition threshold can be tuned in `recognize.py` (`MATCH_THRESHOLD`, default `0.5`) — lower values are stricter.

## Author

Shravan Pawar  — Computer Engineering, Pravara Rural Engineering College (PREC), Loni
BATCH 2024-28 !!
