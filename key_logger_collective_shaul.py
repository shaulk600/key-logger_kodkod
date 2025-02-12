from abc import ABC, abstractmethod
from typing import List
class IKeyLogger(ABC):
 @abstractmethod
 def start_logging(self) -> None:
 pass

 @abstractmethod
 def stop_logging(self) -> None:
 pass

 @abstractmethod
 def get_logged_keys(self) -> List[str]:
 pass

#2

# iwriter.py
from abc import ABC, abstractmethod
class IWriter(ABC):
@abstractmethod
def send_data(self, data: str, machine_name: str) -> None:
pass

#3
class Encryptor:
    pass


#4
class KeyLoggerManager:
    pass

#5
class NetworkWriter:

   #תוצאה נדרשת
#send_data(data: str, machine_name: str) -> None

   pass

#חלק 2 בניית Backend

