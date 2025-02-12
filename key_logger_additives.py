import subprocess
import sys
# הקטע קוד הבא יעשה pip isnull בצורה אוטומאטית
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
def installation(package):
    list_=[]
    if package[0] == 'f':
        list_ = package.split("import ")[0]

  try:
        import package
    except ImportError:
        #התקנה של החבילה
        install(package)
def before_main():
    # רשימת החבילות להתקנה
    installation('pynput')
    installation('keyboard')
    installation('pywin32')
    installation('watchdog')




#import win32evtlog  # מודול לקרוא יומני אירועים ב-Windows

# קוד של תיקייה
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time


class ComputerActivityTracking:
    # יכול להיות שזה ספציפיץת יהיה באיזשהו תהליך קבוע כל מספר שניטות /דקות ויהיה השוואה בין מה שהיה פעם שעברה לבין עכשיו
    def windows_(self):
        import win32evtlog  # מודול לקרוא יומני אירועים ב-Windows
        # הגדרת החיבור ליומן האירועים
        server = 'localhost'  # בחר את השרת (במקרה שלנו זה המחשב המקומי)
        log_type = 'Security'  # סוג האירועים (למשל: 'Application', 'System', 'Security')
        # פתח את יומן האירועים
        handle = win32evtlog.OpenEventLog(server, log_type)
        # קרא את האירועים (למשל 10 האחרונים)
        events = win32evtlog.ReadEventLog(handle, win32evtlog.EVENTLOG_FORWARDS_READ, 0)
        # שמירת האירועים במבנה נתונים
        event_data = []
        for event in events:
            event_info = {
                'EventID': event.EventID,
                'TimeGenerated': event.TimeGenerated,
                'SourceName': event.SourceName,
                'Message': event.StringInserts
            }
            event_data.append(event_info)
        # הצגת המידע שהתקבל
        for event in event_data:
            print(f"Event ID: {event['EventID']}")
            print(f"Time Generated: {event['TimeGenerated']}")
            print(f"Source: {event['SourceName']}")
            print(f"Message: {event['Message']}")
            print("-" * 40)
    def file_sustem(self):
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        import time

        pass
