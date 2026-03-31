import logging
from pathlib import Path
from config import image , bg_img
from gui import gui
from capture import text_capture
import pytesseract
import platform
import os

if platform.system() == "Windows":
    tesseract_path = os.path.join(
        os.environ["LOCALAPPDATA"],
        "Programs",
        "Tesseract-OCR",
        "tesseract.exe"
    )
elif platform.system() == "Linux":
    tesseract_path = "/usr/bin/tesseract"
else:
    tesseract_path = None
    

pytesseract.pytesseract.tesseract_cmd = tesseract_path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"), 
        logging.StreamHandler()             
    ]
)

log = logging.getLogger(__name__)


if __name__ == "__main__":
    gui(image,bg_img)

