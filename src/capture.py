import subprocess
import pyautogui as ag
import platform
import os
import logging

log = logging.getLogger(__name__)

def take_shot(x,y,w,h):
    log.info("Taking Screenshot.")
    shot = ag.screenshot(region=(x, y, w, h))
    os.makedirs("assets", exist_ok=True)
    shot.save("assets/image.png")
    log.info("Screenshot saved.")



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
    take_shot(x,y,w,h)


def get_img_windows():
    import pygetwindow as gw
    target_title = "TypeRacer"
    x, y, w, h = None, None, None, None

    windows = gw.getWindowsWithTitle(target_title)
    if windows:
        window = windows[0]
        x, y, w, h = window.left, window.top, window.width, window.height

        # Take the screen shot
        take_shot(x,y,w,h)
    else:
        log.error("Window not found")
        return



def capture():
    os_name = platform.system()

    if os_name == "Windows":
        log.info("Windows Detected.")
        get_img_windows()

    elif os_name == "Linux":
        log.info("Linux user Detected - btw.")
        get_img_linux()
        
    elif os_name == "Darwin":
        log.info("Macos is not supported - Switch to linux")
    else:
        log.error(f"Unsupported Sysmte {os_name}")

capture()