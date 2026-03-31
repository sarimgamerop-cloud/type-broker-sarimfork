import re
import logging

log = logging.getLogger(__name__)

import pytesseract 
import easyocr
from textblob import TextBlob
import cv2


def text_fetch(img):

    gray_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    _, clean_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # type: ignore
    # cv2.imshow('threshold Image', clean_img)
    # cv2.waitKey(0) # Waits for a key event
    # cv2.destroyAllWindows()

    text = pytesseract.image_to_string(clean_img,config="--psm 4")
    text = text.replace("\n"," ")
    # 1. Find the last occurrence of '0wpm' or 'Owpm'
    # Using a greedy regex `.*` ensures we skip all previous players' wpm scores
    match = re.search(r'.*(?:0wpm|Owpm|pyOwpm)\s+(.*)', text, flags=re.DOTALL)
    
    if not match:
        log.warning("Pattern not found in OCR output")
        return ""
        
    raw_paragraph = match.group(1)
    
    # 2. Clean up the trailing boilerplate text
    # OCR creates variations of "change display format", so we match the common prefixes
    footer_pattern = r'(change display|charge display|crangec|Type the above|eo ay format).*'
    
    # Remove the footer and strip leading/trailing whitespace
    clean_paragraph = re.sub(footer_pattern, '', raw_paragraph, flags=re.DOTALL | re.IGNORECASE).strip()
    
    # 3. Handle minor OCR artifacts (like the stray "hb " in example 4)
    # This removes isolated 1-2 letter lowercase words at the very beginning
    clean_paragraph = re.sub(r'^[a-z]{1,2}\s+', '', clean_paragraph)
    
    # 4. Remove leading symbols like {}[]\/| etc from the start
    clean_paragraph = re.sub(r'^[\s\d\[\]\(\)\|\\/\-_{}]+', '', clean_paragraph)
    
    return clean_paragraph

# Gonna Work on Captcha Later

def get_captcha_text(img):

    def captcha_clean(image): #Done
        global final_img 
        
        #gray_img = cv2.imread(img, 0)
        #blur = cv2.GaussianBlur(gray_img ,(5,5),0)
        #final_img = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)[1] 
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

        # 1. Resize (helps OCR a lot)
        img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) # type: ignore

        # 2. Denoise
        img = cv2.GaussianBlur(img, (5, 5), 0)

        # 4. Threshold (binarize)
        _, final_img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)


        #cv2.imshow('threshold Image', final_img)
        #cv2.waitKey(0) # Waits for a key event
        #cv2.destroyAllWindows()

    global cp_text
    reader = easyocr.Reader(['en'])   
    result = reader.readtext(img,detail=0)
    final_text = " ".join(result) # type: ignore
    
    # Remove leading non-alphanumeric characters and common symbols

    final_text = re.sub(r"^[\s\d\[\]\(\)\|\\/\-_]+", "", final_text)

    #text = re.sub(r"[{}\[\]_]", "", text)
    
    text = re.sub(r"\s+", " ", final_text).strip()
    cp_text = str(TextBlob(text).correct())






