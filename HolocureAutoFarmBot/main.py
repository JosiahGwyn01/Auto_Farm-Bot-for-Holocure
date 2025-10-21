from main_menu import run_main_menu_script
from in_game import run_in_game_script
import time
import keyboard
import os
import pyautogui

class GameState:
    def __init__(self,confidence=0.7):
        self.confidence = confidence
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def detect_state(self):
        main_menu_path = os.path.join(self.script_dir,'images','indicators','main_menu_indicator.png')
        in_game_path = os.path.join(self.script_dir,'images','indicators','in_game_indicator.png')

        try:
            if pyautogui.locateOnScreen(main_menu_path, confidence=self.confidence):
                return "Main Menu"
        except pyautogui.ImageNotFoundException:
            pass

        try:
            if pyautogui.locateOnScreen(in_game_path, confidence=self.confidence):
                return "In Game"
        except pyautogui.ImageNotFoundException:
            pass

        return "Unknown"

def main():
    print("Holocure Auto Farm Bot(Mumei)")
    print("Press 's' to start the bot or 'q' to terminate program")
    
    while True:
        if keyboard.is_pressed('s'):
            print("Starting Program...")
            
            # Continuous state checking loop
            while not keyboard.is_pressed('q'):
                print("Detecting Game State...")
                time.sleep(1)
                state_detector = GameState()
                current_state = state_detector.detect_state()
                time.sleep(2)
                if current_state == 'Main Menu':
                    run_main_menu_script()
                elif current_state == 'In Game':
                    run_in_game_script()  
                else:
                    print("Unknown state, waiting...")
                    time.sleep(2)
                    
            break  
            
        elif keyboard.is_pressed('q'):
            print("Terminating Program...")
            return
            
        time.sleep(0.1)
    
    print("Program Terminated")
    
if __name__ == "__main__":
    main()

