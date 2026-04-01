# Type-Broker

Type-Broker is a Python script with a Tkinter graphical interface to automate typing on [TypeRacer](https://play.typeracer.com/). It works by finding the TypeRacer window, taking a screenshot, performing OCR to extract the text, and then automatically typing it out.

> ⚠️ **Disclaimer: STRICTLY FOR EDUCATIONAL AND LEARNING PURPOSES.** 
> This project was created solely for learning about Optical Character Recognition (OCR), computer vision, and GUI automation with Python. It is not intended to be used to cheat or disrupt competitive environments. Use responsibly.

This Work on my Machine
You have to change xyz coordinates in the respective **config.py** so it work on your machine. **( See the documentation for details )**

## Requirements

To run this project, you will need the following system and Python dependencies installed. 

### System Dependencies
The automation relies on X11 tools for window manipulation and screenshots.
* `pytesseract`
* `pygetwindow`
* `pillow` Required for tkinter services.
* `textblob` Spelling Correction for accuracy.
* `opencv-python`
* `tesseract-ocr` (Required for PyTesseract OCR processing)
* `easyocr` ()
* `wmctrl` (Required to locate the TypeRacer window coordinates)
* `gnome-screenshot` (or another screenshot utility compatible with `pyautogui` for windows.)
* **Note:** This project relies on `wmctrl` and `pyautogui`, which generally require an **Xorg (X11)** display server and may not work natively on Wayland.

## System requirment for Windows
The pytesseract and tesseract-ocr only defines the tesseract module for the system level install which is needed for windows platform install the following
native tesseract program for it to work correctly as it need the `tesseract.exe` : 
[`GitHUB`](https://github.com/UB-Mannheim/tesseract/wiki)
Download the Specific Version and install it on your computer or refer to the automatic install scripts.

### Python Requirements
* Python 3.12 or newer.
* Recommendation: Use [`uv`](https://github.com/astral-sh/uv) for fast package management.

## Installation and Usage

### Standard Installation (Ubuntu/Debian)

1. **Install system dependencies**:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr wmctrl gnome-screenshot python3-tk
   ```
**Alternate Method : ** Use the *automatic install* scripts in the `scripts\` folder.

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

## Windows 10/11 using Automatic Dependencies Install Script:

Use the *automatic install* scripts in the `scripts\` folder.
after the dependencies are installed refer to the **Running the App** page down below.
**Note:** *if the automatic scripts are not working try installing them manually using python pip package manager and install tesseract by the link
given in **System Requirments for Windows** at the top.* 

### Running the App

1. Run the script:
   ```bash
   python main.py
   ```
2. Open your browser and go to a TypeRacer match. Ensure the window title contains "TypeRacer".
3. In the Type-Broker GUI:
   * Click **Fetch** when the race text is visible (this triggers the screenshot and OCR).
   * Click **Start Typing** to start Typing.

## Tested Environments

This program has been developed and validated on the following setups:

* ✅ **Ubuntu 24.04 GNOME (Xorg)**
* ✅ **Window 10**
* 🔄 **NixOS 26.05 (Yarara) x86_64 unstable** (Testing in progress)

## Contributor:

Special thanks to [sarimgamerop](https://github.com/sarimgamerop-cloud) for contributing the beautiful GUI layout and Windows support.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
