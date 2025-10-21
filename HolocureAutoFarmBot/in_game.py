import os

class Ingame:
    def __init__(self, confidence = 0.63):
        self.confidence = confidence
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
    
    def temp_state(self):
        print("In_Game")

def run_in_game_script():
    print("Checking...")
    ingame = Ingame()
    ingame.temp_state()
