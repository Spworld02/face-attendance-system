@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"
"C:\Users\DELL\face-attendance-system\face-attendance-system\venv\Scripts\python.exe" -c "import sys; print('PY:', sys.executable); print('VER:', sys.version)" 
