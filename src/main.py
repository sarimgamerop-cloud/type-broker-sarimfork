# from gui import gui 
import logging
from pathlib import Path

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



'''
Change these Variable based on your display and Preferences
'''

clean_paragraph = None

project_root = Path(__file__).parent


typing_speed = 0.05
captcha_typing_speed = 0.02
start_test_button = (480,515)
captcha_window = (214, 384, 516, 176)
captcha_typing_panel = (430,603)


if __name__ == "__main__":
    # gui()
    pass

