import time
import logging

import pyautogui

from config import typing_speed

log = logging.getLogger(__name__)



def types_the_text(text):
    if not text:
        log.warning("No text to type - please fetch text first")
        return
    time.sleep(2)
    log.info("Typing..")
    pyautogui.typewrite(text, typing_speed)
    log.info("Typing Completed..")


# def solve_captcha():
#     #get image 
#     get_captcha() #Done
#     # clean image 
#     captcha_clean("cap.png") #Done

#     #fetch the text and print 
#     get_text(final_img) #Done
    
#     click(430,603)
#     print("Typing")
#     typewrite(cp_text, interval=0.01)
#     press('tab')
#     time.sleep(0.1)
#     press('enter')
#     print("Typing Completed")