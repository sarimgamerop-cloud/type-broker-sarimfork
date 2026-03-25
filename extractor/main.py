import pytesseract
from PIL import Image
from pathlib import Path
from time import sleep
from pynput.keyboard import Key,Controller
from time import sleep
project_root = Path(__file__).parent.parent # give the location of folder

img_loc =  project_root / "assets" / "image.png"


text = pytesseract.image_to_string(Image.open(img_loc))

keyboard = Controller()
sleep(4)
keyboard.type(text)