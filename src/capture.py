import subprocess
import platform
import os
import time
import logging
from config import os


# pip modules 
from pyautogui import click , screenshot

# local files 
from config import start_test_button, captcha_window, project_root  

log = logging.getLogger(__name__)

def take_shot(x,y,w,h,img_name):
    shot = screenshot(region=(x, y, w, h))
    assets_dir = project_root / "assets"
    assets_dir.mkdir(exist_ok=True)
    shot.save(str(assets_dir / f"{img_name}.png"))
    log.info("Screen Shot Captured")



def get_img_linux():
    '''
    Run wmctrl and get cordinates of Typeracer Window and Take Screenshot
    '''
    target_title = "TypeRacer"
    output = subprocess.check_output(["wmctrl", "-l", "-G"]).decode("utf-8")
    window_data = None
    for line in output.splitlines():
        if target_title in line:
            window_data = line.split()
            break
    if window_data is None:
        log.error("Window not found")
        return
    
    x = int(window_data[2])
    y = int(window_data[3])
    w = int(window_data[4])
    h = int(window_data[5])

    # Take the screen shot
    take_shot(x,y,w,h,"image")


def get_img_windows():
    import pygetwindow as gw
    target_title = "TypeRacer"
    x, y, w, h = None, None, None, None

    windows = gw.getWindowsWithTitle(target_title) # type: ignore
    if windows:
        window = windows[0]
        x, y, w, h = window.left, window.top, window.width, window.height

        # Take the screen shot
        take_shot(x,y,w,h,"image")
    else:
        log.error("Window not found")
        return

def get_captcha(): #Done
    '''
    Click on Start Test button and capture Image
    '''
    click(start_test_button)
    time.sleep(1) # Wait for image to load
    '''
    Logic: the captcha always come one same poistion with same site - based on window postion
    So screenshot take picture of captcha - the region value very on machine to machine
    '''
    take_shot(captcha_window[0],captcha_window[1],captcha_window[2],captcha_window[3],"captcha")

def text_capture():
    global os
    os_name = platform.system()

    if os_name == "Windows":
        log.info("Windows Detected.")
        os = "windows"
        get_img_windows()

    elif os_name == "Linux":
        log.info("Linux user Detected - btw.") # xD
        os = "linux"
        get_img_linux()
        
    elif os_name == "Darwin":
        log.info("Macos is not supported - Switch to linux") # OpRoast
    else:
        log.error(f"Unsupported Sysmte {os_name}")
