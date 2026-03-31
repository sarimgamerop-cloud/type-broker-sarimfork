@echo off
REM Windows Dependency Installer for Type-Broker

echo ========================================
echo Type-Broker Windows Installer
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM List of required packages
set "PACKAGES=pytesseract pyautogui pygetwindow pillow easyocr textblob opencv-python"

echo Installing dependencies...
echo.

for %%p in (%PACKAGES%) do (
    pip show %%p >nul 2>&1
    if errorlevel 1 (
        echo [INSTALLING] %%p
        pip install %%p
        if errorlevel 1 (
            echo [FAILED] Could not install %%p
        ) else (
            echo [OK] %%p installed
        )
    ) else (
        echo [SKIP] %%p already installed
    )
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.

REM Check for Tesseract
set "TESSERACT_PATH=%LOCALAPPDATA%\Programs\Tesseract-OCR\tesseract.exe"

where tesseract >nul 2>&1
if errorlevel 1 (
    if exist "%TESSERACT_PATH%" (
        echo [OK] Tesseract OCR found at %TESSERACT_PATH%
    ) else (
        echo [WARNING] Tesseract OCR not found
        echo Please install from: https://github.com/UB-Mannheim/tesseract/wiki
        echo Default install path: %TESSERACT_PATH%
    )
) else (
    echo [OK] Tesseract OCR is installed and in PATH
)

pause
