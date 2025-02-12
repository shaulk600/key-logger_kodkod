from abc import ABC, abstractmethod
from pynput import keyboard

class KeyLoggerService:
    def __init__(self):
        self.running = True

    @abstractmethod
    def start(self):
        pass


    def stop(self,key):
        if key == keyboard.Key.esc:
            print("\n יציאה מה-Keylogger...")
            self.running = False
            return False

    def get_gson(self,data):
        pass

class KeyLoggerManager:
    pass

class FileWriter:
    pass

class NetworkWriter:
    pass

class Encryptor:
    pass
