@echo off

where python3 >nul 2>nul
if %errorlevel% neq 0 (
    echo Python 3 n'est pas installé. Veuillez l'installer avant de continuer.
    pause
    exit /b
)

pip install -r requirements.txt
python3 -m PyInstaller --onefile --icon=resources/images/icon.ico --name=SweePy SweePy.py
pause