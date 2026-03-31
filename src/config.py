"""
Configuration variables for Type-Broker
Change these based on your display and preferences
"""

from pathlib import Path

project_root = Path(__file__).parent.parent

image = project_root / "assets" / "image.png"
bg_img = project_root / "assets" / "bg.jpg"
typing_speed = 0.05
captcha_typing_speed = 0.02
start_test_button = (480, 515)
captcha_window = (243, 195, 655, 330)
captcha_typing_panel = (430, 603)
os = ""
tesseract_path = None
