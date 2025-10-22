import pydirectinput
import pyautogui
import keyboard
import time
import os

class DetectEnemy:
    def  __init__(self, confidence = 0.7):
        self.confidence = confidence
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

    def detect_enemy(self):
        
        enemy_path = os.path.join(self.script_dir,'images','indicators',)

def main():
    print("Enemy_Detector_Prototype")
    print("Press 's' to start the Detector, Press 'q' to terminate the program...")
    
    while True:
        if keyboard.is_pressed('s'):
            print("Starting the Enemy Detector")
            

        elif keyboard.is_pressed('q'):
            print('Terminating the Program...')
            return

        time.sleep(0.5)
    
    print("Program Terminated")



if __name__ == "__main__":
    main()
