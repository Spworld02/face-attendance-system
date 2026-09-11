@echo off
"C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel cmake
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install dlib
@echo off
@echo Running vcvars64
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
set LOG_PATH=%~dp0install_dlib_venv.log
@echo Upgrading pip/setuptools/wheel/cmake... > "%LOG_PATH%"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel cmake --verbose >> "%LOG_PATH%" 2>&1
@echo Installing dlib... >> "%LOG_PATH%"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -m pip install dlib --verbose >> "%LOG_PATH%" 2>&1
@echo Install log: %LOG_PATH%
type "%LOG_PATH%"
