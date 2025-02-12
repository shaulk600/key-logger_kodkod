from abc import ABC, abstractmethod
import json


class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass


class FileWriter(IWriter):
    def __init__(self, filename = "output.json"):
        self.filename = filename

    def send_data(self, data: str, machine_name: list) -> None:
        try:
            with open(self.filename, encoding="utf-8") as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        entry = {"תאריך ושעה": data, "התוכן": machine_name}
        existing_data.append(entry)


        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False)

#כדי להפעיל את הפונקציה צריכים שם קובץ שמסתיים בגיסון
#לדוגמא
#writer = FileWriter("log.gson")
#writer.send_data("12,01,2025-12:35",[1,5,9,58,2,8])

