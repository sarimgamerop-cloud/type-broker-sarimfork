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


project_root = Path(__file__).parent # give the location of folder
img_loc = project_root /   "image.png"

'''
Change these Variable based on your display and Preferences
'''

typing_speed = 0.05
captcha_typing_speed = 0.02
start_test_button = (480,515)
captcha_window = (214, 384, 516, 176)
captcha_typing_panel = (430,603)

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
    typewrite(text, typing_speed)
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

# --------------- GUI -------------------

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

    # Solve Captcha
    solve_cp = tk.Button(root, text="Solve Captcha",bg="blue", fg="white",command=lambda : solve_captcha())
    solve_cp.pack()
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
    '''
    Fetch Text from captcha using easyocr and clean it little bit
    '''
    global cp_text
    reader = easyocr.Reader(['en'])   
    result = reader.readtext(img,detail=0)
    final_text = " ".join(result)
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

    # click on Typing Panel of captcha
    click(captcha_typing_panel)
    print("Typing")
    typewrite(cp_text, captcha_typing_speed)
    press('tab')
    time.sleep(0.1)
    press('enter')
    print("Typing Completed")
gui()

