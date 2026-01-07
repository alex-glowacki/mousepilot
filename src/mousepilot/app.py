# src/mousepilot/app.py

# Standard library
import time
from datetime import datetime, timedelta

# Third-party
import pyautogui


def main():
    end_time = datetime.now() + timedelta(minutes=120)  # Minutes to move mouse.
    
    while datetime.now() < end_time:
        pyautogui.moveRel(0, 500, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveRel(500, 0, duration=0.5)
        time.sleep(0.25)
        pyautogui.moveRel(0, -500, duration=0.5)
        pyautogui.click()
        time.sleep(0)
        pyautogui.moveRel(-500, 0, duration=0.5)
        time.sleep(1)
        
        pyautogui.FAILSAFE = True