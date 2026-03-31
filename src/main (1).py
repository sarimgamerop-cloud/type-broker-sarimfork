import pytesseract
from PIL import Image
from pathlib import Path
from time import sleep
from pyautogui import typewrite , screenshot, click , press
import re
import subprocess
import cv2 # pyright: ignore[reportMissingImports]
import time 
import tkinter as tk
import easyocr
from textblob import TextBlob
import sys
# for windows only
import pygetwindow as gw
from tkinter import ttk
from PIL import Image, ImageTk  # For background image support

# Explicitly set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Sarim\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



def get_img():
    target_title = "TypeRacer"
    x, y, w, h = None, None, None, None

    # Checks the Operating System and fallback to supported modules:

    if sys.platform == 'win32':
        windows = gw.getWindowsWithTitle(target_title)
        if windows:
            window = windows[0]
            x, y, w, h = window.left, window.top, window.width, window.height
        else:
            print(f"Window '{target_title}' not found on Windows.")
            return
    elif sys.platform.startswith('linux'):
        try:
            output = subprocess.check_output(["wmctrl", "-l", "-G"]).decode("utf-8")
            window_data = None
            for line in output.splitlines():
                if target_title in line:
                    window_data = line.split()
                    break
            if window_data is None:
                print(f"Window '{target_title}' not found on Linux.")
                return
            x = int(window_data[2])
            y = int(window_data[3])
            w = int(window_data[4])
            h = int(window_data[5])
        except FileNotFoundError:
            print("wmctrl not found. Please install it (e.g., 'sudo apt-get install wmctrl').")
            return
        except Exception as e:
            print(f"Error getting window data on Linux: {e}")
            return
    else:
        print(f"Unsupported operating system: {sys.platform}")
        return
    
    # screenshots the region
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
    typewrite(text,typing_speed)
    print("Typing Completed")

def fetch(img, start_typing_btn):
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

    if clean_paragraph:
        start_typing_btn.config(state=tk.NORMAL)
    
    return print(clean_paragraph)

def start(start_typing_btn):
    get_img()
    img_cleaning(img_loc)
    fetch(dst, start_typing_btn)

# --------------- GUI -------------------

def gui(background_image_path=None):
    root = tk.Tk()
    root.title("Type-Broker (EarlyDevelopment)")
    root.geometry("500x350")  # Increased size for better spacing
    root.resizable(False, False)  # Fixed window size for better layout

    # =========================
    # Background Setup
    # =========================
    if background_image_path:
        bg_image = Image.open(background_image_path)
        bg_image = bg_image.resize((500, 350), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # =========================
    # Style Setup for Modern Buttons
    # =========================
    style = ttk.Style(root)
    style.configure(
        "TButton",
        font=("Helvetica", 12, "bold"),
        foreground="white",
        background="#4CAF50",  # Modern green
        padding=10
    )
    style.map(
        "TButton",
        background=[('active', '#45a049')]  # Hover effect
    )

    # =========================
    # Container Frame (for centering buttons)
    # =========================
    frame = tk.Frame(root, bg="", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Center frame in window

    # Start typing button
    start_typing = ttk.Button(
        frame,
        text="Start Typing",
        state=tk.DISABLED,
        command=lambda: types(clean_paragraph)
    )
    start_typing.grid(row=0, column=0, pady=10, sticky="ew")

    # Fetch button
    fetch_btn = ttk.Button(
        frame,
        text="Fetch",
        command=lambda: start(start_typing)
    )
    fetch_btn.grid(row=1, column=0, pady=10, sticky="ew")

    # Solve Captcha button
    solve_cp = ttk.Button(
        frame,
        text="Solve Captcha",
        command=lambda: solve_captcha()
    )
    solve_cp.grid(row=2, column=0, pady=10, sticky="ew")

    # Make buttons expand to fill frame width
    frame.grid_columnconfigure(0, weight=1)

    # =========================
    # Run App
    # =========================
    root.mainloop()

# --------------------- Captcha Related --------------------


def captcha_clean(image): #Done
    global final_img 
    
    #gray_img = cv2.imread(img, 0)
    #blur = cv2.GaussianBlur(gray_img ,(5,5),0)
    #final_img = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)[1] 
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    # 1. Resize (helps OCR a lot)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # 2. Denoise
    img = cv2.GaussianBlur(img, (5, 5), 0)

    # 4. Threshold (binarize)
    _, final_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)


    #cv2.imshow('threshold Image', final_img)
    #cv2.waitKey(0) # Waits for a key event
    #cv2.destroyAllWindows()

def get_captcha(): #Done
    '''
    Click on Start Test button and capture Image
    '''
    click(start_test_button)
    time.sleep(0.9) # Wait for image to load
    '''
    Logic: the captcha always come one same poistion with same site - based on window postion
    So screenshot take picture of captcha - the region value very on machine to machine
    '''
    take_shot = screenshot(region=captcha_window)
    take_shot.save("cap.png")

def get_text(img):
    global cp_text
    reader = easyocr.Reader(['en'])   
    result = reader.readtext(img,detail=0)
    final_text = " ".join(result)
        # Remove leading non-alphanumeric characters and common symbols
    final_text = re.sub(r"^[\s\d\[\]\(\)\|\\/\-_]+", "", final_text)
        #text = re.sub(r"[{}\[\]_]", "", text)
    
    text = re.sub(r"\s+", " ", final_text).strip()
    cp_text = str(TextBlob(text).correct())


def solve_captcha():
    #get image 
    get_captcha() #Done
    # clean image 
    captcha_clean("cap.png") #Done

    #fetch the text and print 
    get_text(final_img) #Done
    
    click(430,603)
    print("Typing")
    typewrite(cp_text, interval=0.01)
    press('tab')
    time.sleep(0.1)
    press('enter')
    print("Typing Completed")
gui()
click(captcha_typing_panel)