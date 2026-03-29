# Type-Broker

Type-Broker is a Python script with a Tkinter graphical interface to automate typing on [TypeRacer](https://play.typeracer.com/). It works by finding the TypeRacer window, taking a screenshot, performing OCR to extract the text, and then automatically typing it out.

> ⚠️ **Disclaimer: STRICTLY FOR EDUCATIONAL AND LEARNING PURPOSES.** 
> This project was created solely for learning about Optical Character Recognition (OCR), computer vision, and GUI automation with Python. It is not intended to be used to cheat or disrupt competitive environments. Use responsibly.

## Requirements

To run this project, you will need the following system and Python dependencies installed. 

### System Dependencies
The automation relies on X11 tools for window manipulation and screenshots.
* `tesseract-ocr` (Required for PyTesseract OCR processing)
* `wmctrl` (Required to locate the TypeRacer window coordinates)
* `gnome-screenshot` (or another screenshot utility compatible with `pyautogui` on your OS)
* **Note:** This project relies on `wmctrl` and `pyautogui`, which generally require an **Xorg (X11)** display server and may not work natively on Wayland.

### Python Requirements
* Python 3.12 or newer.
* Recommendation: Use [`uv`](https://github.com/astral-sh/uv) for fast package management.

Dependencies defined in `pyproject.toml`:
* `opencv-python`
* `pillow`
* `pyautogui`
* `pytesseract`

## Installation and Usage

### Standard Installation (Ubuntu/Debian)

1. **Install system dependencies**:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr wmctrl gnome-screenshot python3-tk
   ```

2. **Setup the Python environment**:
   ```bash
   uv venv
   source .venv/bin/activate
   uv sync
   ```

### NixOS Installation (using Flakes)

If you are using Nix with flakes enabled, a `flake.nix` is already provided. It will bring in `uv`, Python, `wmctrl`, and `gnome-screenshot`.

1. **Enter the development shell**:
   ```bash
   nix develop
   ```
   *The shell hook will automatically create a virtual environment and sync Python dependencies using `uv`.*

### Running the App

1. Run the script:
   ```bash
   python main.py
   ```
2. Open your browser and go to a TypeRacer match. Ensure the window title contains "TypeRacer".
3. In the Type-Broker GUI:
   * Click **Fetch** when the race text is visible (this triggers the screenshot and OCR).
   * Click **Start Typing** when the countdown finishes to automatically type the text.

## Tested Environments

This program has been developed and validated on the following setups:

* ✅ **Ubuntu 24.04 GNOME (Xorg)**
* 🔄 **NixOS 26.05 (Yarara) x86_64 unstable** (Testing in progress)
