@echo off
set LOG=%~dp0install_face_recognition_venv.log
echo Running vcvars64 > "%LOG%"
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat" >> "%LOG%" 2>&1
echo Upgrading pip/setuptools/wheel/cmake... >> "%LOG%"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel cmake --verbose >> "%LOG%" 2>&1
echo Installing face_recognition... >> "%LOG%"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install face_recognition --verbose >> "%LOG%" 2>&1
echo Install complete. Log saved to %LOG% >> "%LOG%"
type "%LOG%"
