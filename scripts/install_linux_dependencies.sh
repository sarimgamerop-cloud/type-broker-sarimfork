#!/bin/bash

# Type-Broker Linux Installer

echo "========================================"
echo "Type-Broker Linux Installer"
echo "========================================"
echo

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed"
    echo "Install with: sudo apt install python3 python3-pip"
    exit 1
fi

echo "[OK] Python3 is installed"
python3 --version
echo

# Detect package manager and installer
USE_UV=false
USE_PIP=false

if command -v uv &> /dev/null; then
    USE_UV=true
    echo "[OK] uv package manager found"
elif command -v pip3 &> /dev/null; then
    USE_PIP=true
    echo "[OK] pip3 found"
elif command -v pip &> /dev/null; then
    USE_PIP=true
    echo "[OK] pip found"
else
    echo "[ERROR] Neither uv nor pip found"
    echo "Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo "Or install pip: sudo apt install python3-pip"
    exit 1
fi
echo

# Install system dependencies
echo "========================================"
echo "Installing System Dependencies"
echo "========================================"

if command -v apt &> /dev/null; then
    echo "Detected APT (Ubuntu/Debian)"
    echo "Installing: wmctrl, tesseract-ocr, scrot"
    sudo apt update
    sudo apt install -y wmctrl tesseract-ocr scrot
elif command -v dnf &> /dev/null; then
    echo "Detected DNF (Fedora)"
    sudo dnf install -y wmctrl tesseract
elif command -v pacman &> /dev/null; then
    echo "Detected Pacman (Arch)"
    sudo pacman -S --noconfirm wmctrl tesseract
elif command -v zypper &> /dev/null; then
    echo "Detected Zypper (openSUSE)"
    sudo zypper install -y wmctrl tesseract-ocr
else
    echo "[WARNING] Could not detect package manager"
    echo "Please install manually: wmctrl, tesseract-ocr"
fi
echo

# Install Python packages
echo "========================================"
echo "Installing Python Packages"
echo "========================================"

PACKAGES="pytesseract pyautogui pygetwindow pillow easyocr textblob opencv-python"

if [ "$USE_UV" = true ]; then
    echo "Using uv to install packages..."
    for pkg in $PACKAGES; do
        if uv pip show "$pkg" &> /dev/null; then
            echo "[SKIP] $pkg already installed"
        else
            echo "[INSTALLING] $pkg"
            uv pip install "$pkg"
        fi
    done
elif [ "$USE_PIP" = true ]; then
    echo "Using pip to install packages..."
    for pkg in $PACKAGES; do
        if pip3 show "$pkg" &> /dev/null 2>&1 || pip show "$pkg" &> /dev/null 2>&1; then
            echo "[SKIP] $pkg already installed"
        else
            echo "[INSTALLING] $pkg"
            pip3 install "$pkg" || pip install "$pkg"
        fi
    done
fi

echo
echo "========================================"
echo "Installation Complete!"
echo "========================================"
