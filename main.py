import pytesseract
from PIL import Image
from pathlib import Path
from time import sleep
from pyautogui import typewrite , screenshot
import re
import subprocess
import cv2 # pyright: ignore[reportMissingImports]
import time 
import tkinter as tk

# TODO: Next Bypass Cheat Detection Captcha 

project_root = Path(__file__).parent # give the location of folder
img_loc = project_root /   "image.png"
testing = project_root / "assets" /  "6.png"


def get_img():
    target_title = "TypeRacer"
    output = subprocess.check_output(["wmctrl", "-l", "-G"]).decode("utf-8")
    window_data = None
    for line in output.splitlines():
        if target_title in line:
            window_data = line.split()
            break
    if window_data is None:
        print(f"Window '{target_title}' not found")
        return
    
    x = int(window_data[2])
    y = int(window_data[3])
    w = int(window_data[4])
    h = int(window_data[5])

    shot = screenshot(region=(x, y, w, h))
    shot.save("image.png")

def img_cleaning(img):
    global dst
    gray_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    _, dst = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # cv2.imshow('threshold Image', dst)
    # cv2.waitKey(0) # Waits for a key event
    # cv2.destroyAllWindows()


def types(text):
    sleep(2)
    print("Typing")
    typewrite(text, interval=0.01)
    print("Typing Completed")

def fetch(img):
    global clean_paragraph
    text = pytesseract.image_to_string(img,config="--psm 4")
    text = text.replace("\n"," ")
    # 1. Find the last occurrence of '0wpm' or 'Owpm'
    # Using a greedy regex `.*` ensures we skip all previous players' wpm scores
    match = re.search(r'.*(?:0wpm|Owpm|pyOwpm)\s+(.*)', text, flags=re.DOTALL)
    
    if not match:
        return print("Pattern not found.")
        
    raw_paragraph = match.group(1)
    
    # 2. Clean up the trailing boilerplate text
    # OCR creates variations of "change display format", so we match the common prefixes
    footer_pattern = r'(change display|charge display|crangec|Type the above|eo ay format).*'
    
    # Remove the footer and strip leading/trailing whitespace
    clean_paragraph = re.sub(footer_pattern, '', raw_paragraph, flags=re.DOTALL | re.IGNORECASE).strip()
    
    # 3. Handle minor OCR artifacts (like the stray "hb " in example 4)
    # This removes isolated 1-2 letter lowercase words at the very beginning
    clean_paragraph = re.sub(r'^[a-z]{1,2}\s+', '', clean_paragraph)
    
    return print(clean_paragraph)

def start():
    get_img()
    img_cleaning(img_loc)
    fetch(dst)

def gui():
    root = tk.Tk()
    root.title("The Title")
    root.geometry("400x300")  # width x height
    # Get img and clean and fetch
    fetch = tk.Button(root, text="Fetch",bg="blue", fg="white",command=lambda : start())
    fetch.pack()
    # start typing yooo!
    start_typing = tk.Button(root, text="Start Typing",bg="blue", fg="white",command=lambda :types(clean_paragraph))
    start_typing.pack()

    # Fetch Text from Captcha
    fetch_captcha = tk.Button(root, text="Fetch Captcha",bg="blue", fg="white",command=lambda :types(clean_paragraph))
    fetch_captcha.pack()
    # Start Typing Captcha
    solve_captcha = tk.Button(root, text="Solve Captcha",bg="blue", fg="white",command=lambda :types(clean_paragraph))
    solve_captcha.pack()
    root.mainloop()

def get_text(img):
    text = pytesseract.image_to_string(img,config="--psm 3")
    # text = text.replace("\n"," ")
    return print(text)


def captcha_clean(img):
    global dst
    gray_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    _, dst = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY) # without cv2.THRESH_OTSU it give better results in captcha

    cv2.imshow('threshold Image', dst)
    cv2.waitKey(0) # Waits for a key event
    cv2.destroyAllWindows()


captcha_clean("6.png")