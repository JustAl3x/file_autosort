from watchdog.events import FileSystemEventHandler
import os
import time

downloads_folder = "/Users/username/Downloads"
image_folder = "/Users/username/Desktop/images"
uni_folder = "/Users/username/Desktop/uni"
misc_folder = "/Users/username/Desktop/misc"

class DownloadsHandler(FileSystemEventHandler):
    imageCount = 1
    uniCount = 1

    def on_modified(self, event):
        #give time for file to fully download
        time.sleep(3)
        for filename in os.listdir(downloads_folder):
            src = downloads_folder + "/" + filename
            dest = ""

            historicalSize = -1
            #this try/except waits until the file size stops increasing
            #before moving it, i.e. the download has complete.
            try:
                while (historicalSize != os.stat(filename).st_size):
                    historicalSize = os.stat(filename).st_size
            except FileNotFoundError:
                print("Download finished.")
            
            #RE, CCSEP, CC mentioned below are all reference to specific classes
            if (".png" in filename or ".jpg" in filename or ".jpeg" in filename):
                dest = image_folder + "/" + filename
            elif ("RE" in filename):
                dest = uni_folder + "/" + "RE/" + filename
            elif ("CCSEP" in filename):
                dest = uni_folder + "/" + "CCSEP/" + filename
            elif ("CC" in filename):
                dest = uni_folder + "/" + "CC/" + filename
            elif (".pdf" in filename):
                dest = uni_folder + "/" + filename
            else:
                dest = misc_folder + "/" + filename

            try:
                os.rename(src, dest)
                if (os.stat(dest).st_size == 0):
                    os.remove(dest)
            except FileNotFoundError: 
                print("File not found")
