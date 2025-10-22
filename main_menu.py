# Imports
from pyautogui import *
import pyautogui
import time
import keyboard
import os
import pydirectinput


class MainMenu:
    def __init__(self,confidence=0.63):
        self.confidence = confidence
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.images = [
            'start_button.png',
            'mumei_portrait.png',
            'endless_mode.png'
        ]

    def mainmenu_nav(self):
        print("Navigating to Endless Mode (Mumei)...")

        for i, image_name in enumerate(self.images):
            if keyboard.is_pressed('q'):
                return False
            
            if not self._menu_step(image_name, i):
                
                return False
            
    def _menu_step(self, image_name, step_number):
        step_names = {
            0: "Start Button Select",
            1: "Mumei Portrait Select",
            2: "Endless Mode Select"
        }        
    
        print(f"Starting {step_names[step_number]}...")

        image_path = os.path.join(self.script_dir, 'images', 'main_menu', image_name)

        try:
            element = pyautogui.locateOnScreen(image_path, confidence=self.confidence)

            if element:
                print(f"Found {step_names[step_number]}")
                self._click_element(element, step_number)
                return True
            else:
                print(f"Not Found {step_names[step_number]}")
                return False
        except Exception as e:
            print(e)
            

    def _click_element(self, element, step_number):
        center = pyautogui.center(element)
        print(f"Coordinates: {center}")

        pyautogui.moveTo(center)
        pydirectinput.press('space')

        if step_number == 0:
            time.sleep(0.5)
        elif step_number == 2:
            time.sleep(0.5)
            pydirectinput.press('space')
            pydirectinput.press('space')
        else:
            time.sleep(0.5)

def run_main_menu_script():
    print("running script in...")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)

    nav = MainMenu()
    print("Bot Starting....")
    nav.mainmenu_nav()