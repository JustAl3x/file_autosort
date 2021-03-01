import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from handler import DownloadsHandler
downloads_folder = "/Users/username/Downloads"

def main():
    event_handler = DownloadsHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=True)
    observer.start()

    try:
        while (True):
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

main()
