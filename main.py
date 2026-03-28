import pytesseract
from PIL import Image
from pathlib import Path
from time import sleep
from pyautogui import typewrite
project_root = Path(__file__).parent # give the location of folder

img_loc =  project_root / "assets" / "image.png"

def fetch():
    global text
    print("Fetching text from image..")
    text = pytesseract.image_to_string(Image.open(img_loc))
    print("Fetching Completed")
    print("Cleaning...")
    text = text.replace("\n"," ")
    print("Cleaning Completed...")

def types():
    sleep(2)
    print("Typing")
    typewrite(text, interval=0.07)
    print("Typing Completed")